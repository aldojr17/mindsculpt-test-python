import redis as redispy

import config
import utils

cfg = config.get_config()
logger = utils.get_logger()


class RedisClient:

    def __init__(self):
        self.host = cfg.redis_host
        self.port = cfg.redis_port
        self.password = cfg.redis_password
        self._client = None

    @property
    def client(self):
        if not self._client:
            self._client = redispy.Redis(
                host=self.host,
                port=self.port,
                password=self.password
            )

        return self._client

    def get(self, key):
        logger.info(f"get cache with key: {key}")
        return self.client.get(key)


redis_client = RedisClient()
