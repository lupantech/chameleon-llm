# Chameleon: Plug-and-Play Compositional Reasoning with GPT-4

![Science Problems](https://img.shields.io/badge/Task-Science_Problems-blue) 
![Science Problems](https://img.shields.io/badge/Task-MathQA-blue) 
![Science Problems](https://img.shields.io/badge/Task-TableQA-blue) 
![Chain-of-Thought](https://img.shields.io/badge/Model-Tool_Use-green) 
![GPT-4](https://img.shields.io/badge/Model-GPT--4-green) 
![LLMs](https://img.shields.io/badge/Model-LLMs-green)

Code for the Paper "[Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.xxxxx)".

:bell: If you have any questions or suggestions, please don't hesitate to let us know. You can directly email [Pan Lu](https://lupantech.github.io/) using the email address lupantech@gmail.com, comment on the [Twitter](), or post an issue on this repository.



## 💥 News 💥

- **[2023.04.19]** Our paper is now available at https://arxiv.org/abs/2304.xxxxx.



## About Chameleon

**Chameleon** is a plug-and-play compositional reasoning framework that augments LLMs to help address these challenges. **Chameleon** synthesizes programs to compose various tools, including LLM models, off-the-shelf vision models, web search engines, Python functions, and rule-based modules tailored to user interests. Built on top of an LLM as a natural language planner, **Chameleon** infers the appropriate sequence of tools to compose and execute in order to generate a final response. 

![showcase_scienceqa](assets/showcase_scienceqa.png)

We showcase the adaptability and effectiveness of **Chameleon** on two tasks: ScienceQA and TabMWP. Notably, **Chameleon** with GPT-4 achieves an 86.54% accuracy on ScienceQA, significantly improving upon the best published few-shot model by 11.37%; using GPT-4 as the underlying LLM, Chameleon achieves a 17.8% increase over the state-of-the-art model, leading to a 98.78% overall accuracy on TabMWP. Further studies suggest that using GPT-4 as a planner exhibits more consistent and rational tool selection and is able to infer potential constraints given the instructions, compared to other LLMs like ChatGPT.

For more details, you can find our project page [here](https://chameleon-llm.github.io/) and our paper [here](assets/chameleon2023lu.pdf).



## Run on ScienceQA

Run **Chameleon** (GPT-4):

```sh
cd run_scienceqa

python run.py \
--model chameleon \
--label chameleon_gpt4 \
--policy_engine gpt-4 \
--kr_engine gpt-4 \
--qg_engine gpt-4 \
--sg_engine gpt-4 \
--test_split test \
--test_number -1
```

Run **Chameleon** (ChatGPT):

```sh
cd run_scienceqa

python run.py \
--model chameleon \
--label chameleon_gpt4 \
--policy_engine gpt-3.5-turbo \
--kr_engine gpt-3.5-turbo \
--qg_engine gpt-3.5-turbo \
--sg_engine gpt-3.5-turbo \
--test_split test \
--test_number -1
```

Run CoT GPT-4:

```sh
cd run_scienceqa

python run.py \
--model cot \
--label cot_gpt4 \
--sg_engine gpt-4 \
--test_split test \
--test_number -1
```



## Run Chameleon on TabMWP

Run **Chameleon** (GPT-4):

```sh
## GPT-4, Chameleon
python run.py \
--model chameleon \
--label chameleon_gpt4 \
--test_split test \
--tl_engine gpt-4 \
--rl_engine gpt-4 \
--cl_engine gpt-4 \
--tv_engine gpt-4 \
--kr_engine gpt-4 \
--sg_engine gpt-4 \
--pg_engine gpt-4 \
--test_number -1 \
--rl_cell_threshold 18 \
--cl_cell_threshold 18
```

Run **Chameleon** (ChatGPT):

```sh
## GPT-4, Chameleon
python run.py \
--model chameleon \
--label chameleon_chatgpt \
--test_split test \
--tl_engine gpt-3.5-turbo \
--rl_engine gpt-3.5-turbo \
--cl_engine gpt-3.5-turbo \
--tv_engine gpt-3.5-turbo \
--kr_engine gpt-3.5-turbo \
--sg_engine gpt-3.5-turbo \
--pg_engine gpt-3.5-turbo \
--test_number -1 \
--rl_cell_threshold 18 \
--cl_cell_threshold 18
```

Run CoT GPT-4:

```sh
## GPT-4, CoT
python run.py \
--model cot \
--label cot_gpt4 \
--test_split test \
--sg_engine gpt-4 \
--test_number -1
```

Run PoT GPT-4:

```sh
## GPT-4, PoT
python run.py \
--model pot \
--label pot_gpt4 \
--test_split test \
--pg_engine gpt-4 \
--test_number -1
```





## :warning: Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

This work is licensed under a [MIT License](http://creativecommons.org/licenses/by-nc-sa/4.0/).



## More Examples

![showcase_tabmwp_long](assets/showcase_tabmwp_long.png)



## :white_check_mark: Cite

If you find Chameleon useful for your your research and applications, please cite using this BibTeX:

```latex
@article{chameleon2023lu,
  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu Song-Chun and Gao, Jianfeng},
  journal={arXiv preprint arXiv:2304.xxxxx},
  year={2023}
}
```
