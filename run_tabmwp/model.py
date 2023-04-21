import os
import re
import sys
import json
import openai

# add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utilities import *
from demos import prompt_policy, prompt_rl, prompt_cl, prompt_tv, prompt_kr, prompt_pg, prompt_sg

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

class solver:

    def __init__(self, args):
        # arguments
        for key, value in vars(args).items():
            setattr(self, key, value)

        # external arguments
        self.api_key = openai.api_key
        self.examples, self.pids = self.load_data()

    def load_data(self):
        # load test data
        examples = json.load(open(os.path.join(self.data_root, f"problems_{self.test_split}.json")))
        pids = list(examples.keys())
        if self.test_number > 0:
            if self.test_number < len(pids):
                pids = pids[:self.test_number]
                examples = {key: value for key, value in examples.items() if key in pids}
        return examples, pids

    def build_prompt_for_policy(self):
        # demo prompt
        demo_prompt = prompt_policy.prompt.strip()

        # test prompt
        table = self.cache["example"]["table"]
        question = self.cache["example"]["question"]
        test_prompt = f"Table:\n{table}\n\nQuestion: {question}\n\nModules: "

        # full prompt
        full_prompt = demo_prompt + "\n\n" + test_prompt
        return test_prompt, full_prompt

    def update_modules(self, _modules):
        default_modules = ["program_generator", "program_verifier", "program_executor", "answer_generator"]
        
        try:
            modules = eval(_modules.lower().strip())
            # answer_generator
            assert "answer_generator" in modules

            # program_generator < program_verifier < program_executor
            if ["program_verifier"] in modules:
                assert modules.index(["program_generator"]) - modules.index(["program_verifier"]) == -1
            if ["program_executor"] in modules:
                assert modules.index(["program_generator"]) - modules.index(["program_executor"]) in [-1,-2]

        except:
            modules = default_modules

        # if modules not in valid_candidates:
        #     modules = default_modules

        if "program_generator" in modules and "program_verifier" in modules:
            index_pg = modules.index("program_generator")
            index_pv = modules.index("program_verifier")
            if index_pv - index_pg == 1:
                modules.remove("program_verifier")
                modules[index_pg] = "program_generator_and_verifier"

        return modules

    def predict_modules(self):
        # get the module input
        test_prompt, full_prompt = self.build_prompt_for_policy()
        messages=[
            {"role": "user", "content": full_prompt},
        ]

        # execute the module
        modules = get_chat_response(messages, self.api_key, self.policy_engine, self.policy_temperature, self.policy_max_tokens)
        modules = self.update_modules(modules)

        # update the cache
        self.cache["modules:input"] = test_prompt
        self.cache["modules:output"] = modules
        return modules

    def row_lookup(self):
        # get the module input
        question = self.cache["example"]["question"]
        table = self.cache["example"]["table"]
        context = self.cache["example"]["context"] if "context" in self.cache["example"] else ""
        row_num = self.cache["example"]["row_num"]
        column_num = self.cache["example"]["column_num"]
        cell_num = row_num * column_num

        # if row_num <=3 or cell_num <= 12:
        if row_num <= self.rl_row_threshold or cell_num <= self.rl_cell_threshold:
            test_prompt = None
            simple_table = table

        else: 
            demo_prompt = prompt_rl.prompt.strip()
            # test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\nSimplified Table:\n"
            if context != "":
                test_prompt = f"Question: {question}\n\nTable:\n{table}\n\n{context}\n\nSimplified Table:\n"
            else:
                test_prompt = f"Question: {question}\n\nTable:\n{table}\n\nSimplified Table:\n"

            full_prompt = demo_prompt + "\n\n" + test_prompt
            messages=[
                {"role": "user", "content": full_prompt},
            ]
            # execute the module
            if self.rl_cand == 1:
                simple_table = get_chat_response(messages, self.api_key, self.rl_engine, self.rl_temperature, self.rl_max_tokens)
            else:
                simple_tables = get_chat_response(messages, self.api_key, self.rl_engine, self.rl_temperature, self.rl_max_tokens, self.rl_cand)
                simple_table = max(simple_tables, key=simple_tables.count)

        # update the cache
        self.cache["example"]["table"] = simple_table # update the table!!
        self.cache["row_lookup:input"] = test_prompt
        self.cache["row_lookup:output"] = simple_table
        return test_prompt, simple_table
    
    def column_lookup(self):
        # get the module input
        question = self.cache["example"]["question"]
        table = self.cache["example"]["table"]
        context = self.cache["example"]["context"] if "context" in self.cache["example"] else ""
        row_num = self.cache["example"]["row_num"]
        column_num = self.cache["example"]["column_num"]
        cell_num = row_num * column_num

        # if column_num <= 2 or cell_num <= 12:
        if column_num <= self.cl_col_threshold or cell_num <= self.cl_cell_threshold:
            test_prompt = None
            simple_table = table

        else:
            demo_prompt = prompt_cl.prompt.strip()
            # test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\nSimplified Table:\n"
            if context != "":
                test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\n{context}\n\nSimplified Table:\n"
            else:
                test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\nSimplified Table:\n"
            full_prompt = demo_prompt + "\n\n" + test_prompt
            messages=[
                {"role": "user", "content": full_prompt},
            ]
            # execute the module
            simple_table = get_chat_response(messages, self.api_key, self.cl_engine, self.cl_temperature, self.cl_max_tokens)

        # update the cache
        self.cache["example"]["table"] = simple_table # update the table!!
        self.cache["column_lookup:input"] = test_prompt
        self.cache["column_lookup:output"] = simple_table
        return test_prompt, simple_table
    
    def table_verbalizer(self):
        # get the module input
        question = self.cache["example"]["question"]
        table = self.cache["example"]["table"]
        context = self.cache["example"]["context"] if "context" in self.cache["example"] else ""

        demo_prompt = prompt_tv.prompt.strip()
        # test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\nTable description:\n"
        if context != "":
            test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\n{context}\n\nTable description:\n"
        else:
            test_prompt = f"Question: {question}\n\nTable:\n\n{table}\n\nTable description:\n"
        full_prompt = demo_prompt + "\n\n" + test_prompt
        messages=[
            {"role": "user", "content": full_prompt},
        ]

        # execute the module
        verbalization = get_chat_response(messages, self.api_key, self.tv_engine, self.tv_temperature, self.tv_max_tokens)
        context += f"\n\nTable description: {verbalization}".strip()

        # update the cache
        self.cache["example"]["context"] = context
        self.cache["table_verbalizer:input"] = test_prompt
        self.cache["table_verbalizer:output"] = verbalization
        return test_prompt, verbalization

    def knowledge_retrieval(self):
        # get the module input
        question = self.cache["example"]["question"]
        table = self.cache["example"]["table"]
        context = self.cache["example"]["context"] if "context" in self.cache["example"] else ""

        demo_prompt = prompt_kr.prompt.strip()
        # test_prompt = f"Table:\n\n{table}\n\nQuestion: {question}\n\nKnowledge:\n"
        if context != "":
            test_prompt = f"Table:\n\n{table}\n\n{context}\n\nQuestion: {question}\n\nKnowledge:\n"
        else:
            test_prompt = f"Table:\n\n{table}\n\nQuestion: {question}\n\nKnowledge:\n"

        full_prompt = demo_prompt + "\n\n" + test_prompt
        messages=[
            {"role": "user", "content": full_prompt},
        ]

        # execute the module
        knowledge = get_chat_response(messages, self.api_key, self.kr_engine, self.kr_temperature, self.kr_max_tokens)
        context += f"\n\nKnowledge:\n{knowledge}".strip()

        # update the cache
        self.cache["example"]["context"] = context
        self.cache["knowledge_retrieval:input"] = test_prompt
        self.cache["knowledge_retrieval:output"] = knowledge
        return test_prompt, knowledge
    
    def build_prompt_for_pg(self):
        question = self.cache["example"]["question"]
        unit = self.cache["example"]["unit"]
        choices = self.cache["example"]["choices"]
        table = self.cache["example"]["table"]
        table_title = self.cache["example"]["table_title"]
        context = self.cache["example"]["context"] if "context" in self.cache["example"] else ""

        if choices:
            demo_prompt = prompt_pg.prompt_choice.strip()
        else:
            demo_prompt = prompt_pg.prompt_free.strip()
        
        if table_title:
            instruction = f"Read the following table regarding {table_title} and then write Python code to answer a question:"
        else:
            instruction = "Read the following table and then write Python code to answer a question:"
        
        if unit:
            question += f" (Unit: {unit})"
        if choices:
            question += f" Please select from the following options: {choices}."

        if choices:
            solution = "# Python Code, return 'ans'. Make sure that 'ans' is a string selected from the options in the question"
        else:
            solution = "# Python Code, return 'ans'. Make sure that 'ans' is a number"
        
        if context != "":
            test_prompt = f"{instruction}\n\n{table}\n\n{context}\n\n{question}\n\n{solution}"
        else:
            test_prompt = f"{instruction}\n\n{table}\n\n{question}\n\n{solution}"

        full_prompt = demo_prompt + "\n\n" + test_prompt
        return test_prompt, full_prompt

    def program_generator(self):
        # get the module input
        test_prompt, full_prompt = self.build_prompt_for_pg()
        messages=[
            {"role": "user", "content": full_prompt},
        ]

        # excute the module
        program = get_chat_response(messages, self.api_key, self.pg_engine, self.pg_temperature, self.pg_max_tokens)

        # update the cache
        self.cache["program"] = program
        self.cache["program_generator:input"] = test_prompt
        self.cache["program_generator:output"] = program
        return test_prompt, program

    def _verify_program(self, program):
        # check if the program is valid
        if not isinstance(program, str):
            return False
        if isinstance(program, str):
            if "ans =" not in program:
                return False
        _output = safe_execute(program)
        if _output in (None, "", [], {}):
            return False
        return True

    def program_verifier(self):
        if "program" in self.cache:
            program = self.cache["program"]
        else:
            return None, False
        
        # excute the module
        success = self._verify_program(program)

        # update the cache
        self.cache["program_verifier:output"] = success
        return program, success

    def program_generator_and_verifier(self):
        # get the module input
        patience = self.pv_patience
        test_prompt, full_prompt = self.build_prompt_for_pg()
        messages=[
            {"role": "user", "content": full_prompt},
        ]

        # excute the module
        program = None
        success = False
        count = 0
        while count < patience and not success:
            if self.pg_temperature < 0.1 and count > 0:
                _temperature = min(self.pg_temperature + 0.1, 1.0)
            else:
                _temperature = self.pg_temperature
            program = get_chat_response(messages, self.api_key, self.pg_engine, _temperature, self.pg_max_tokens)
            success = self._verify_program(program)
            count += 1
            # if not success:
            #     print(program)

        # update the cache
        self.cache["program"] = program
        self.cache["program_generator_and_verifier:input"] = test_prompt
        self.cache["program_generator_and_verifier:output"] = program
        return test_prompt, program

    def program_executor(self):
        if "program" in self.cache:
            program = self.cache["program"]
        else:
            return None, False
        
        # excute the module
        ans = safe_execute(program)

        # update the cache
        self.cache["program_executor:output"] = ans
        return program, ans

    def build_prompt_for_sg(self):
        question = self.cache["example"]["question"]
        unit = self.cache["example"]["unit"]
        choices = self.cache["example"]["choices"]
        table = self.cache["example"]["table"]
        table_title = self.cache["example"]["table_title"]
        context = self.cache["example"]["context"] if "context" in self.cache["example"] else ""

        if choices:
            demo_prompt = prompt_sg.prompt_choice.strip()
        else:
            demo_prompt = prompt_sg.prompt_free.strip()
        
        if table_title:
            instruction = f"Read the following table regarding {table_title} and then answer a question:"
        else:
            instruction = "Read the following table and then answer a question:"
        
        if unit:
            question += f" (Unit: {unit})"
        if choices:
            question += f" Please select from the following options: {choices}."

        if context != "":
            test_prompt = f"{instruction}\n\n{table}\n\n{context}\n\n{question}\n\nSolution: "
        else:
            test_prompt = f"{instruction}\n\n{table}\n\n{question}\n\nSolution: "

        full_prompt = demo_prompt + "\n\n" + test_prompt
        return test_prompt, full_prompt

    def solution_generator(self):
        # get the module input
        test_prompt, full_prompt = self.build_prompt_for_sg()
        messages=[
            {"role": "user", "content": full_prompt},
        ]

        # excute the module
        success = False
        patience = self.sg_patience
        count = 0
        while count < patience and not success:
            if self.sg_temperature < 0.1 and count > 0:
                _temperature = min(self.sg_temperature + 0.1, 1.0)
            else:
                _temperature = self.sg_temperature

            solution = get_chat_response(messages, self.api_key, self.sg_engine, _temperature, self.sg_max_tokens)

            pattern = re.compile(r"The answer is ([\s\S]+).$") # "The answer is XXXXX.",
            res = pattern.findall(solution)
            if len(res) > 0:
                success = True
            count += 1

        # update the cache
        self.cache["solution_generator:input"] = test_prompt
        self.cache["solution_generator:output"] = solution
        return test_prompt, solution
    
    def answer_generator(self):
        # get the module input
        if "program_executor:output" in self.cache and self.cache["program_executor:output"] is not None:
            ans = self.cache["program_executor:output"]

        elif "solution_generator:output" in self.cache and self.cache["solution_generator:output"] is not None:
            output = self.cache["solution_generator:output"]
            pattern = re.compile(r"The answer is ([\s\S]+).$") # "The answer is XXXXX.",
            res = pattern.findall(output)
            if len(res) > 0:
                ans = res[-1].strip()
            else:
                ans = output
        else:
            ans = None

        # excute the module
        answer = floatify_ans(ans)

        # update the cache
        self.cache["answer_generator:input"] = ans
        self.cache["answer_generator:output"] = answer
        self.cache["prediction"] = answer
        return ans, answer
