import utils
from connection.constant import HttpMethod

from config.config import Config
import requests


logger = utils.get_logger()


class RequestClient:

    def __init__(self) -> None:
        self.config = Config()

    def get(self, path, params=None):
        url = f"{self.config.protocol}://{self.config.host}{path}"

        logger.info(
            f"method={HttpMethod.GET}|url={url}|params={params}"
        )

        response = requests.get(url=url, params=params)

        logger.info(
            f"status_code={response.status_code}|body={response.text}"
        )

        return response

