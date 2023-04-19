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
            # text context
            if results[index]["example"]['hint'] != "":
                
                res_pd.loc[index, 'text_context'] = True
            else:
                res_pd.loc[index, 'text_context'] = False
            # image context
            if results[index]["example"]['image'] == "image.png":
                res_pd.loc[index, 'image_context'] = True
            else:
                res_pd.loc[index, 'image_context'] = False
            # no context
            if results[index]["example"]['hint'] == "" and results[index]["example"]['image'] != "image.png":
                res_pd.loc[index, 'no_context'] = True
            else:
                res_pd.loc[index, 'no_context'] = False

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

        'acc_nat': get_acc_with_contion(res_pd, 'subject', 'natural science'),
        'acc_sol': get_acc_with_contion(res_pd, 'subject', 'social science'),
        'acc_lan': get_acc_with_contion(res_pd, 'subject', 'language science'),

        'acc_txt': get_acc_with_contion(res_pd, 'text_context', True),
        'acc_img': get_acc_with_contion(res_pd, 'image_context', True),
        'acc_no': get_acc_with_contion(res_pd, 'no_context', True),
        
        'acc_grade_1_6': get_acc_with_contion(res_pd, 'grade', ["grade2", "grade3", "grade4", "grade5", "grade6"]),
        'acc_grade_7_12': get_acc_with_contion(res_pd, 'grade', ["grade7", "grade8", "grade9", "grade10", "grade11", "grade12"]),
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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file', type=str, default="../data/scienceqa/problems.json")
    parser.add_argument('--result_root', type=str, default="../results/scienceqa")
    parser.add_argument('--result_files', type=str, default="chameleon_gpt4_test_cache.jsonl")
    args = parser.parse_args()
    args = parser.parse_args()

    ############################################
    # # CoT ChatGPT, 78.31%
    # args.result_files = "cot_chatgpt_test_cache.jsonl"
    
    # # CoT GPT-4, 83.99%
    # args.result_files = "cot_gpt4_test_cache.jsonl"

    # # Chameleon ChatGPT, 79.93%
    # args.result_files = "chameleon_chatgpt_test_cache.jsonl"

    # # Chameleon GPT-4, 86.54%
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
