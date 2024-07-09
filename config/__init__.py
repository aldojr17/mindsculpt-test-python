from .config import Config
from .query_data import QueryData

config = Config()
query_data = QueryData()


def get_config():
    return config


def get_query_data():
    return query_data
