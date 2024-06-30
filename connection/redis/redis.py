import json

from connection.redis import redis_client


class RedisUtils:
    @staticmethod
    def get_models_key():
        key = "models"
        record = redis_client.get(key)
        return json.loads(record)
