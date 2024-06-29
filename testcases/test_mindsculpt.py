from connection.request_client.request_client import RequestClient
from testcases.base import MindsculptBase
from http import HTTPStatus


class TestMindsculpt(MindsculptBase):

    def test_get_models(self):
        response = RequestClient().get(path=self.PATH_GET_MODELS)
        assert response.status_code == HTTPStatus.OK

