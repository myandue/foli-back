from .infra.redis import ChatContextStore

repository = ChatContextStore()


def set_chat_context(session_id, context, ttl=3600):
    repository.append(session_id, context, ttl)


def get_chat_context(session_id):
    return repository.get_recent_5(session_id)
