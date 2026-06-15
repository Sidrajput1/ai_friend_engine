chat_session = {}

def get_history(session_id):

    if session_id not in chat_session:
        chat_session[session_id] = []
    
    return chat_session[session_id]


def add_message(session_id , role , content):

    history = get_history(session_id)

    history.append({
        "role":role,
        "content":content
    })