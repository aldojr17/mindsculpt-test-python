import os
import yaml # type: ignore


class Config:
    def __init__(self) -> None:
        with open(os.path.dirname(os.path.dirname(__file__)) + "/config.yaml", "r") as file:
            config = yaml.safe_load(file)

        mindsculpt_config = config.get("mindsculpt", {})
        self.host = mindsculpt_config.get("api", {}).get("host", "")
        self.protocol = mindsculpt_config.get("api", {}).get("protocol", "")
        