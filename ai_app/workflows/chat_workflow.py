from prompts.generat_prompt import build_general_prompt
from services.ask_llm import ask_llm
from services.ollama_service import ask_ollama


def run(question,history):
    #print("Using General Chat Workflow")
   

    # prompt = build_general_prompt(
    #     question,
    #     history
    # )
    # instead of this single prompt we need to pass to function
    system_prompt = build_general_prompt(
        history
    )

    print("\n===== SYSTEM PROMPT =====")
    print(system_prompt)
    print("=========================\n")

    print("\n===== USER MESSAGE =====")
    print(question)
    print("=========================\n")
    response = ask_llm(
        system_prompt,
        question
    )
    # print("\n====== GENERAL PROMPT ======")
    # print(repr(prompt))
    # print("============================")
   
    return response