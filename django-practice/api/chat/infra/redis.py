import redis
from django.conf import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_CHAT_DB,
    decode_responses=True,
)


class ChatContextStore:
    def get(self, session_id):
        return redis_client.get(f"chat:ctx:{session_id}")

    def set(self, session_id, context, ttl=1800):
        redis_client.setex(f"chat:ctx:{session_id}", ttl, context)

    def delete(self, session_id):
        redis_client.delete(f"chat:ctx:{session_id}")
