from .request_client.request_client import RequestClient

client = RequestClient()


def get_request_client():
    return client
