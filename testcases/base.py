import random

import config
import utils

query_data = config.get_query_data()
logger = utils.get_logger()


class MindsculptBase:
    PATH_GET_MODELS = "/models"
    PATH_GENERATE = "/generate"

    RATIO_1_1 = "1:1"
    RATIO_2_3 = "2:3"
    RATIO_3_2 = "3:2"
    RATIO_9_16 = "9:16"
    RATIO_16_9 = "16:9"

    def generate_width_and_height(self, ratio):
        if ratio == self.RATIO_1_1:
            return {
                "width": 1280,
                "height": 1280
            }
        elif ratio == self.RATIO_2_3:
            return {
                "width": 1280,
                "height": 1920
            }
        elif ratio == self.RATIO_3_2:
            return {
                "width": 1280,
                "height": 853
            }
        elif ratio == self.RATIO_9_16:
            return {
                "width": 1280,
                "height": 2276
            }
        elif ratio == self.RATIO_16_9:
            return {
                "width": 1280,
                "height": 720
            }

    @staticmethod
    def generate_query():
        sentence = random.choice(query_data.sentences.get("data")).get("sentence", "football player")
        logger.info(f"query: {sentence}")
        return sentence

    def generate_body(self, ratio=RATIO_1_1):
        body = {
            "query": self.generate_query(),
            "negative_prompt_unclip": "bright colors",
            "model_id": 4
        }

        body.update(self.generate_width_and_height(ratio))

        return body
