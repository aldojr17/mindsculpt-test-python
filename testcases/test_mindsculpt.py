from jsonschema import validate

from connection.redis.redis import RedisUtils
from connection.request_client.request_client import RequestClient
from testcases.base import MindsculptBase
from http import HTTPStatus


class TestMindsculpt(MindsculptBase):

    def test_get_models(self):
        response = RequestClient().get(path=self.PATH_GET_MODELS)
        assert response.status_code == HTTPStatus.OK

        result = response.json()

        validate(instance=result, schema=self.GET_MODELS_SCHEMA)

        record = RedisUtils.get_models_key()
        assert record is not None

        assert record == result.get("data", {})
