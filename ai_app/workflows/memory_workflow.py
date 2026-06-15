from prompts.memory_prompt import build_memory_prompt
from services.ask_llm import ask_llm

def run(question):
    print("Using Memory Workflow")
    # prompt = build_memory_prompt(
    #     question
    # )

    # return ask_llm(prompt)

    system_prompt = build_memory_prompt()

    return ask_llm(
        system_prompt,
        question
    )