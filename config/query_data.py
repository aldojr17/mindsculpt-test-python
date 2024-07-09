import json
import os


class QueryData:

    def __init__(self):
        with open(os.path.dirname(os.path.dirname(__file__)) + "/sentences.json", "r") as file:
            self.sentences = json.load(file)
