import os
import sys
import json
import argparse
import random
from tqdm import tqdm

# add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

from utilities import *
from model import solver


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', type=str, default='../data/tabmwp')
    parser.add_argument('--output_root', type=str, default='../results')
    parser.add_argument('--model', type=str, default='chameleon', choices=['cot', 'pot', 'chameleon'])
    parser.add_argument('--label', type=str, default='chameleon_chatgpt')
    parser.add_argument('--task_name', type=str, default='tabmwp')
    parser.add_argument('--test_split', type=str, default='test1k', 
                        choices=['dev', 'dev1k', 'test', 'test1k'])
    parser.add_argument('--test_number', type=int, default=100)
    parser.add_argument('--seed', type=int, default=0)
    # module prediction
    parser.add_argument('--modules', nargs='+', default=None, help='default modules')
    parser.add_argument('--policy_engine', type=str, default="gpt-3.5-turbo", help='engine for module prediction')
    parser.add_argument('--policy_temperature', type=float, default=0., help='temperature for module prediction')
    parser.add_argument('--policy_max_tokens', type=int, default=128, help='max tokens for module prediction')
    # row lookup
    parser.add_argument('--rl_engine', type=str, default="gpt-3.5-turbo", help='engine for row lookup')
    parser.add_argument('--rl_temperature', type=float, default=0., help='temperature for row lookup')
    parser.add_argument('--rl_max_tokens', type=int, default=256, help='max tokens for row lookup')
    parser.add_argument('--rl_cand', type=int, default=1, help='candidates for row lookup')
    parser.add_argument('--rl_row_threshold', type=int, default=3, help='row number threshold for row lookup')
    parser.add_argument('--rl_cell_threshold', type=int, default=12, help='cell number threshold for row lookup')
    # column lookup
    parser.add_argument('--cl_engine', type=str, default="gpt-3.5-turbo", help='engine for column lookup')
    parser.add_argument('--cl_temperature', type=float, default=0., help='temperature for column lookup')
    parser.add_argument('--cl_max_tokens', type=int, default=256, help='max tokens for column lookup')
    parser.add_argument('--cl_cand', type=int, default=1, help='candidates for column lookup')
    parser.add_argument('--cl_col_threshold', type=int, default=2, help='column number threshold for column lookup')
    parser.add_argument('--cl_cell_threshold', type=int, default=12, help='cell number threshold for column lookup')
    # table verbalizer
    parser.add_argument('--tv_engine', type=str, default="gpt-3.5-turbo", help='engine for table verbalizer')
    parser.add_argument('--tv_temperature', type=float, default=0., help='temperature for table verbalizer')
    parser.add_argument('--tv_max_tokens', type=int, default=512, help='max tokens for table verbalizer')
    # knowledge retrieval
    parser.add_argument('--kr_engine', type=str, default="gpt-3.5-turbo", help='engine for knowledge retrieval')
    parser.add_argument('--kr_temperature', type=float, default=0., help='temperature for knowledge retrieval')
    parser.add_argument('--kr_max_tokens', type=int, default=512, help='max tokens for knowledge retrieval')
    # solution_generator
    parser.add_argument('--sg_engine', type=str, default="gpt-3.5-turbo", help='engine for solution_generator')
    parser.add_argument('--sg_temperature', type=float, default=0., help='temperature for solution_generator')
    parser.add_argument('--sg_max_tokens', type=int, default=512, help='max tokens for solution_generator')
    parser.add_argument('--sg_patience', type=int, default=20, help='patience for solution_generator')
    # program generation
    parser.add_argument('--pg_engine', type=str, default="gpt-3.5-turbo", help='engine for program generation')
    parser.add_argument('--pg_temperature', type=float, default=0.0, help='temperature for program generation')
    parser.add_argument('--pg_max_tokens', type=int, default=256, help='max tokens for program generation')
    # program verifier
    parser.add_argument('--pv_patience', type=int, default=20, help='patience for program verifier')
    # debug
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    print('====Input Arguments====')
    print(json.dumps(vars(args), indent=2, sort_keys=False))
    return args


if __name__ == "__main__":

    args = parse_args()
    random.seed(args.seed)

    # Build the solver
    solver = solver(args)
    print(f"# Number of test examples: {len(solver.examples)}\n")

    # Get the result file
    result_root = f"{args.output_root}/{args.task_name}"
    os.makedirs(result_root, exist_ok=True)
    cache_file = f"{result_root}/{args.label}_{args.test_split}_cache.json"
    cache_jsonl = f"{result_root}/{args.label}_{args.test_split}_cache.jsonl"
    result_file = f"{result_root}/{args.label}_{args.test_split}.json"
    print(result_file)

    count, correct, wrong = 0, 0, 0
    if os.path.exists(result_file):
        print(f"Result file exists: {result_file}")
        with open(result_file, 'r') as f:
            result = json.load(f)
        count = result['count']
        correct = result['correct']
        wrong = result['wrong']
        print(f"Count: {count}, Correct: {correct}, Wrong: {wrong}")
    pids = solver.pids[count:] # only use the remaining problems

    for pid in tqdm(pids):
        solver.cache = {"pid": pid} # clear the cache

        if args.debug or count < 10:
            print("\n\n===================================\n")
            print(f"# [Pid]: {pid}\n") # problem id

        count += 1  # number of current results
        solver.cache["example"] = solver.examples[pid] # get one example 

        # [1] Predict the modules
        if args.modules is not None:
            modules = args.modules
            print(f"# [Modules]\n{modules}\n")
        else:
            if args.model == 'cot':
                modules = ["solution_generator", "answer_generator"]
            elif args.model == 'pot':
                modules = ["program_generator", "program_executor", "answer_generator"]
            elif args.model == 'chameleon':    
                modules = solver.predict_modules()
        modules = [f"solver.{module}" for module in modules]
            
        # [2] Execute the modules 
        if args.debug or count < 10:
            print(f"# [Modules]\n{modules}\n")
            
        for module in modules:
            input, output = eval(module)() # eval the module and update the cache
            if args.debug or count < 10:
                print(f"======== [Module]: {module} ========\n")
                print(f"# [Input]\n{input}\n")
                print(f"# [Output]\n{output}\n")

        # [3] Evaluate the results
        # normalize the number in the text
        answer = solver.cache["example"]["answer"]
        unit = solver.cache["example"]["unit"]
        ans_type = solver.cache["example"]["ans_type"]
        options = solver.cache["example"]["choices"]
        prediction = solver.cache["prediction"]

        answer_norm = normalize_ground_tabmwp(answer, ans_type)
        prediction_norm = normalize_prediction_tabmwp(prediction, options, unit)

        if safe_equal(prediction_norm, answer_norm):
            correct += 1
            true_false = True
        else:
            wrong += 1
            true_false = False

        solver.cache["prediction_norm"] = prediction_norm
        solver.cache["answer_norm"] = answer_norm
        solver.cache["true_false"] = true_false

        if args.debug or count < 10:
            print(f"# [Answer]: {answer_norm}\n")
            print(f"# [Prediction]\n{prediction_norm}\n")
            print(f"# [true_false]\n{true_false}\n")

        acc = correct / count * 100

        # [4] Save the results
        # save the cache by appending
        # print(solver.cache)
        with open(cache_file, "a") as f:
            try:
                f.write(json.dumps(solver.cache, indent=2, separators=(',', ': ')) + "\n")
            except Exception as e:
                print(e)
                print(solver.cache)
        
        with open(cache_jsonl, "a") as f:
            try:
                json.dump(solver.cache, f)
                f.write('\n')
            except Exception as e:
                print(e)
                print(solver.cache)

        # save the result
        result = {'acc': acc, 'correct': correct, 'wrong':wrong, 'count': count, 'args': vars(args)}
        with open(result_file, 'w') as f:
            json.dump(result, f, indent=2, separators=(',', ': '))
