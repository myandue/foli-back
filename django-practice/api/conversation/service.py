import requests
from django.conf import settings

from ..chat.service import set_chat_context, get_chat_context

AI_SERVER_URL = settings.AI_SERVER_URL


def init_conversation_n_get_answer(session_id, document, user_message):
    api_url = f"{AI_SERVER_URL}/api/chat/init"
    params = {"document": document, "user_message": user_message}

    response = requests.post(
        api_url,
        json=params,
    )
    response.raise_for_status()
    # response = {  # Mock response for testing
    #     "answer": "This is a mock answer from AI server."
    # }

    answer = response.json().get("answer", "")
    set_chat_context(session_id=session_id, context=f"user: {user_message}")
    set_chat_context(session_id=session_id, context=f"assistant: {answer}")

    return answer


def get_answer_from_ai(session_id, user_message, document=None):
    if document:
        return init_conversation_n_get_answer(
            session_id, document, user_message
        )

    conversation_history = get_chat_context(session_id)

    api_url = f"{AI_SERVER_URL}/api/chat/message"
    params = {"history": conversation_history, "user_message": user_message}

    response = requests.post(
        api_url,
        json=params,
    )
    response.raise_for_status()
    # response = {  # Mock response for testing
    #     "answer": "This is a mock answer from AI server."
    # }

    answer = response.get("answer", "")
    set_chat_context(session_id=session_id, context=f"user: {user_message}")
    set_chat_context(
        session_id=session_id,
        context=f"assistant: {answer}",
    )

    return answer
