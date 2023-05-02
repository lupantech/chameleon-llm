import time
import random
import openai
import func_timeout
import requests
import numpy as np

from typing import Union, Any
from math import isclose


def safe_execute(code_string: str, keys=None):
    def execute(x):
        try:
            exec(x)
            locals_ = locals()
            if keys is None:
                return locals_.get('ans', None)
            else:
                return [locals_.get(k, None) for k in keys]
        except Exception:
            return None
    try:
        ans = func_timeout.func_timeout(1, execute, args=(code_string,))
    except func_timeout.FunctionTimedOut:
        ans = None
    return ans


def get_codex_response(prompt, api_key, engine="code-davinci-002", temperature=0, max_tokens=256, top_p=1, n=1, patience=10, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            response = openai.Completion.create(engine=engine,
                                                prompt=prompt,
                                                api_key=api_key,
                                                temperature=temperature,
                                                max_tokens=max_tokens,
                                                top_p=top_p,
                                                n=n,
                                                stop=['\n\n'],
                                                frequency_penalty=0,
                                                presence_penalty=0)
            prediction = response["choices"][0]["text"].strip()
            if prediction != "" and prediction != None:
                return prediction
        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


def get_gpt3_response(prompt, api_key, engine="text-davinci-002", temperature=0, max_tokens=256, top_p=1, n=1, patience=100, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            response = openai.Completion.create(engine=engine,
                                                prompt=prompt,
                                                api_key=api_key,
                                                temperature=temperature,
                                                max_tokens=max_tokens,
                                                top_p=top_p,
                                                n=n,
                                                stop=['\n\n'],
                                                frequency_penalty=0,
                                                presence_penalty=0)
            prediction = response["choices"][0]["text"].strip()
            if prediction != "" and prediction != None:
                return prediction
        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


def get_chat_response(messages, api_key, model="gpt-3.5-turbo", temperature=0, max_tokens=256, n=1, patience=100, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            response = openai.ChatCompletion.create(model=model,
                                                messages=messages,
                                                api_key=api_key,
                                                temperature=temperature,
                                                max_tokens=max_tokens,
                                                n=n)
            if n == 1:
                prediction = response['choices'][0]['message']['content'].strip()
                if prediction != "" and prediction != None:
                    return prediction
            else:
                prediction = [choice['message']['content'].strip() for choice in response['choices']]
                if prediction[0] != "" and prediction[0] != None:
                    return prediction

        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


def floatify_ans(ans):
    if ans is None:
        return None
    elif type(ans) == dict:
        ans = list(ans.values())[0]
    elif type(ans) == bool:
        ans = ans
    elif type(ans) in [list, tuple]:
        if not ans:
            return None
        else:
            try:
                ans = float(ans[0])
            except Exception:
                ans = str(ans[0])
    else:
        try:
            ans = float(ans)
        except Exception:
            ans = str(ans)
    return ans

def score_string_similarity(str1, str2):
    if str1 == str2:
        return 2.0
    elif " " in str1 or " " in str2:
        str1_split = str1.split(" ")
        str2_split = str2.split(" ")
        overlap = list(set(str1_split) & set(str2_split))
        return len(overlap) / max(len(str1_split), len(str2_split))
    else:
        return 0.0
        
def normalize_prediction_tabmwp(prediction, options=None, unit=None):
    # the numerical answer
    if isinstance(prediction, float):
        prediction = round(prediction, 3)
        return prediction

    # the string answer
    if isinstance(prediction, str):
        prediction = prediction.replace('$', '')
        if unit:
            prediction = prediction.replace(unit, '')
        prediction = prediction.strip().lower()

        if not options:
            # numeric answer: convert to float
            try:
                if '/' in prediction:
                    prediction = int(prediction.split('/')[0]) / int(prediction.split('/')[1])
                elif ',' in prediction:
                    prediction = float(prediction.replace(',', ''))
                elif '%' in prediction:
                    prediction = float(prediction.split('%')[0]) / 100
                else:
                    prediction = float(prediction)
            except Exception:    
                pass 
 
    # the string answer from choices
    if options:
        options = [x.lower() for x in options]
        if prediction is None:
            prediction = options[0]
        elif isinstance(prediction, str):
            if prediction not in options:
                # find the most similar option
                scores = [score_string_similarity(x, prediction) for x in options]
                max_idx = int(np.argmax(scores)) # json does not recognize NumPy data types
                prediction = options[max_idx]
    return prediction
    
    
def normalize_ground_tabmwp(gt_ans, ans_type=None):
    if ans_type in ['integer_number', 'decimal_number']:
        if '/' in gt_ans:
            gt_ans = int(gt_ans.split('/')[0]) / int(gt_ans.split('/')[1])
        elif ',' in gt_ans:
            gt_ans = float(gt_ans.replace(',', ''))
        elif '%' in gt_ans:
            gt_ans = float(gt_ans.split('%')[0]) / 100
        else:
            gt_ans = float(gt_ans)
    elif ans_type.endswith('_text'):
        gt_ans = str(gt_ans)
    else:
        raise ValueError(ans_type)
    return gt_ans
    

def normalize_ground_scienceqa(gt_ans):
    gt_ans = gt_ans.lower()
    return gt_ans
    
def normalize_prediction_scienceqa(prediction, options=None):
    # the string answer from choices
    if options:
        options = [x.lower() for x in options]
        if prediction is None:
            prediction = options[0]
        elif isinstance(prediction, str):
            if prediction not in options:
                # find the most similar option
                scores = [score_string_similarity(x, prediction) for x in options]
                max_idx = int(np.argmax(scores)) # json does not recognize NumPy data types
                prediction = options[max_idx]
    return prediction

def get_precision(gt_ans: float) -> int:
    precision = 5
    if '.' in str(gt_ans):
        precision = len(str(gt_ans).split('.')[-1])
    return precision
    

def safe_equal(prediction: Union[bool, float, str],
                reference: Union[float, str],
                include_percentage: bool = False,
                is_close: float = False) -> bool:
    if prediction is None:
        return False
    elif type(prediction) == bool:
        # bool questions
        if prediction:
            return reference == 'yes'
        else:
            return reference == 'no'
    elif type(reference) == str and type(prediction) == str:
        # string questions
        prediction = prediction.strip().lower()
        reference = reference.strip().lower()
        return prediction == reference
    else:
        # number questions
        if include_percentage:
            gt_result = [reference / 100, reference, reference * 100]
        else:
            gt_result = [reference]
        for item in gt_result:
            try:
                if is_close:
                    if isclose(item, prediction, rel_tol=0.001):
                        return True
                precision = min(get_precision(prediction), get_precision(item))
                if round(prediction, precision) == round(item, precision):
                    return True
            except Exception:
                continue
        return False


def _validate_server(address):
    if not address:
        raise ValueError('Must provide a valid server for search')
    if address.startswith('http://') or address.startswith('https://'):
        return address
    PROTOCOL = 'http://'
    print(f'No protocol provided, using "{PROTOCOL}"')
    return f'{PROTOCOL}{address}'

def call_bing_search(endpoint, bing_api_key, query, count):
    headers = {'Ocp-Apim-Subscription-Key': bing_api_key}
    params = {"q": query, "textDecorations": True,
              "textFormat": "HTML", "count": count, "mkt": "en-GB"}
    try:
        server = _validate_server(endpoint) # server address
        server_response = requests.get(server, headers=headers, params=params)
        resp_status = server_response.status_code
        if resp_status == 200:
            result = server_response.json()
            return result 
    except:
        pass
    
    return None
    
def parse_bing_result(result):
    responses = []
    try:
        value = result["webPages"]["value"]
    except:
        return responses

    for i in range(len(value)):
        snippet = value[i]['snippet'] if 'snippet' in value[i] else ""
        snippet = snippet.replace("<b>", "").replace("</b>", "").strip()
        if snippet != "":
            responses.append(snippet)
        
    return responses
