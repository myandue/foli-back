from .infra.redis import ChatContextStore

repository = ChatContextStore()


def set_chat_context(session_id, context, ttl=3600):
    repository.set(session_id, context, ttl)
