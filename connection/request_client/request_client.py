from connection.constant import HttpMethod
from utils.logging.logger import Logger

from config.config import Config
import requests


class RequestClient(Logger):

    def __init__(self) -> None:
        super().__init__()
        self.config = Config()

    def get(self, path, params=None):
        url = f"{self.config.protocol}://{self.config.host}{path}"

        self.logger.info(
            f"method={HttpMethod.GET}|url={url}|params={params}"
        )

        response = requests.get(url=url, params=params)

        self.logger.info(
            f"status_code={response.status_code}|body={response.text}"
        )

        return response

