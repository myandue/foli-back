import redis, json
from django.conf import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_CHAT_DB,
    decode_responses=True,
)


class ChatContextStore:
    def append(self, session_id, context, ttl=3600):
        redis_client.rpush(
            f"chat:ctx:{session_id}", json.dumps(context, ensure_ascii=False)
        )
        redis_client.expire(f"chat:ctx:{session_id}", ttl)

    def get_recent_5(self, session_id):
        # 전체: 0 -1, 처음 다섯개: 0 4, 최근 다섯개: -5 -1
        items = redis_client.lrange(f"chat:ctx:{session_id}", -5, -1)
        print(items)
        return [json.loads(item) for item in items]

    def clear(self, session_id):
        redis_client.delete(f"chat:ctx:{session_id}")
