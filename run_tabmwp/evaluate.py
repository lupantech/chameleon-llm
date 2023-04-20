import os
import json
import argparse
import warnings
import pandas as pd

warnings.filterwarnings('ignore')


def get_acc_with_contion(res_pd, key, values):
    if isinstance(values, list):
        total_pd = res_pd[res_pd[key].isin(values)]
    else:
        total_pd = res_pd[res_pd[key] == values]
    correct_pd = total_pd[total_pd['true_false'] == True]
    acc = "{:.2f}".format(len(correct_pd) / len(total_pd) * 100)
    return acc

def read_result_file(result_file):
    if result_file.endswith('.jsonl'):
        with open(result_file) as f:
            results = {}
            for line in f:
                try:
                    data = json.loads(line)
                    results[data["pid"]] = data
                except:
                    # print("Error in line: ", line, "\n")
                    pass
    else:
        result_data = json.load(open(result_file))
        results = result_data["results"]
        
    return results

def get_scores(result_files, data_file):

    if not isinstance(result_files, list):
        result_files = [result_files]

    res_pds = []
    for result_file in result_files:
        # read result file
        results = read_result_file(result_file)
        test_pids = list(results.keys())

        # read data file
        prob_data = json.load(open(data_file))

        # construct pandas data
        prob_data = pd.DataFrame(prob_data).T
        res_pd = prob_data[prob_data.index.isin(test_pids)]  # test set

        # update data
        for index, row in res_pd.iterrows():
            res_pd.loc[index, 'true_false'] = results[index]['true_false']

        # append result pd
        res_pds.append(res_pd)

    # merge all result pds
    res_pd = pd.concat(res_pds)
    num = len(res_pd)
    #assert num == 7686
    print("number of questions:", num)

    # accuracy scores
    acc_average = round(len(res_pd[res_pd['true_false'] == True]) / num * 100, 3)
    #assert acc_average == round(result_data["acc"], 3)

    scores = {
        'acc_average': "{:.2f}".format(acc_average),
        'acc_free': get_acc_with_contion(res_pd, 'ques_type', 'free_text'),
        'acc_mc': get_acc_with_contion(res_pd, 'ques_type', 'multi_choice'),
        'acc_integer': get_acc_with_contion(res_pd, 'ans_type', 'integer_number'),
        'acc_decimal': get_acc_with_contion(res_pd, 'ans_type', 'decimal_number'),
        'acc_extractive': get_acc_with_contion(res_pd, 'ans_type', 'extractive_text'),
        'acc_boolean': get_acc_with_contion(res_pd, 'ans_type', 'boolean_text'),
        'acc_other': get_acc_with_contion(res_pd, 'ans_type', 'other_text'),
        'acc_grade_1_6': get_acc_with_contion(res_pd, 'grade', [1, 2, 3, 4, 5, 6]),
        'acc_grade_7_8': get_acc_with_contion(res_pd, 'grade', [7, 8]),
    }

    return scores


def print_scores(scores):
    latex_output = ""
    print("")
    for key, score in scores.items():
        print(f"{key}: \t{score}")
        latex_output += f"& {score} "
    latex_output += "\\\\"
    print("")
    print(latex_output)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file', type=str, default="../data/tabmwp/problems_test.json")
    parser.add_argument('--result_root', type=str, default="../results/tabmwp")
    parser.add_argument('--result_files', type=str, default="chameleon_chatgpt_test_cache.jsonl")
    args = parser.parse_args()

    ############################################
    # # ChatGPT CoT, 82.03%
    # args.result_files = "cot_chatgpt_test_cache.jsonl"

    # # ChatGPT PoT, 89.49%
    # args.result_files = "pot_chatgpt_test_cache.jsonl"
    
    # # ChatGPT chameleon (ours), 93.27%
    # args.result_files = "chameleon_chatgpt_test_cache.jsonl"

    # # GPT-4 CoT, 90.81%
    # args.result_files = "cot_gpt4_test_cache.jsonl"

    # # GPT-4 PoT, 96.93%
    # args.result_files = "pot_gpt4_test_cache.jsonl"

    # # GPT-4 chameleon (ours), 98.78%
    # args.result_files = "chameleon_gpt4_test_cache.jsonl"
    ############################################

    data_file = args.data_file
    print("Data file: ", data_file)

    result_root = args.result_root
    result_files = args.result_files.split(",")
    result_files = [os.path.join(result_root, result_file.strip()) for result_file in result_files]
    print("Result file: ")
    for result_file in result_files:
        print(result_file)

    scores = get_scores(result_files, data_file)
    print_scores(scores)
