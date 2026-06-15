from fastapi import FastAPI
from api.schemas import ChatRequest
from rag.rag_engine import build_prompt
from services.ask_llm import ask_llm
from chat.session_manager import get_history
from chat.session_manager import add_message
from router.query_router import classify_question

from prompts.generat_prompt import build_general_prompt
from prompts.history_prompt import build_history_prompt
from prompts.memory_prompt import build_memory_prompt
from fastapi.middleware.cors import CORSMiddleware


from workflows import (
    history_workflow,
    memory_workflow,
    chat_workflow
)
app = FastAPI()

app.add_middleware(
     CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

def home():
    return{
        "message": "AI Friend API Running"
    }

@app.post("/chat")

def chat(request:ChatRequest):

    route = classify_question(
    request.message
    )

    print("Route:", route)

    history = get_history(
        request.session_id
    )

    add_message(
        request.session_id,
        "user",
        request.message
    )

    # print("\n===== HISTORY =====")
    # print(history)
    # print("===================\n")


    # prompt = build_prompt(
        
    #     request.message,
    #     history
    # )
    if route == "history":

        # prompt = build_history_prompt(
        #     request.message,
        #     history
        # )
        
        response = history_workflow.run(
            request.message,
            history
        )

    elif route == "memory":

        # prompt = build_memory_prompt(
        #     request.message
        # )

        response = memory_workflow.run(
            request.message
        )

    else:

        # prompt = build_general_prompt(
        #     request.message,
        #     history
        # )

        response = chat_workflow.run(
            request.message,
            history
        )


    # response = ask_llm(response)

    add_message(
        request.session_id,
        "assistant",
        response
    )
    
    # return{
    #     "message_received":request.message
    # }
    return {
        "response":response
    }

