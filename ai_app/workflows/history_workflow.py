from prompts.history_prompt import build_history_prompt

from services.ask_llm import ask_llm

def run(question,history):

    print("Using History Workflow")
    # prompt = build_history_prompt(
    #     question,
    #     history
    # )

    # return ask_llm(prompt)
    system_prompt = build_history_prompt(
        history
    )
    return ask_llm(
        system_prompt,
        question
    )
