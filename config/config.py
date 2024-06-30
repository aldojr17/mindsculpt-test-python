import os

import yaml


class Config:

    def __init__(self) -> None:
        with open(os.path.dirname(os.path.dirname(__file__)) + "/config.yaml", "r") as file:
            config = yaml.safe_load(file)

        mindsculpt_config = config.get("mindsculpt", {})
        api_config = mindsculpt_config.get("api", {})
        db_config = mindsculpt_config.get("db", {})
        redis_config = mindsculpt_config.get("redis", {})
        self.host = api_config.get("host", "")
        self.protocol = api_config.get("protocol", "")
        self.db_host = db_config.get("host", "")
        self.db_port = db_config.get("port", 0)
        self.db_username = db_config.get("username", "")
        self.db_password = db_config.get("password", "")
        self.db_name = db_config.get("db_name", "")
        self.redis_host = redis_config.get("host", "")
        self.redis_port = redis_config.get("port", 0)
        self.redis_password = redis_config.get("password", "")
