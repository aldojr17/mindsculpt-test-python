import requests

import config
import utils
from connection.constant import HttpMethod

cfg = config.get_config()
logger = utils.get_logger()


class RequestClient:

    def __init__(self) -> None:
        self.host = cfg.host
        self.protocol = cfg.protocol

    def get(self, path, params=None):
        url = f"{self.protocol}://{self.host}{path}"

        logger.info(
            f"method={HttpMethod.GET}|url={url}|params={params}"
        )

        response = requests.get(url=url, params=params)

        self.log_response(response)

        return response

    def post(self, path, body):
        url = f"{self.protocol}://{self.host}{path}"

        logger.info(
            f"method={HttpMethod.POST}|url={url}|body={body}"
        )

        response = requests.post(url=url, json=body)

        self.log_response(response)

        return response

    @staticmethod
    def log_response(response):
        logger.info(
            f"status_code={response.status_code}|response={response.text}"
        )
