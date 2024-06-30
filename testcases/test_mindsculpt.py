from http import HTTPStatus

from jsonschema import validate

import connection
from connection.redis.redis import RedisUtils
from testcases.base import MindsculptBase


class TestMindsculpt(MindsculptBase):

    def test_get_models(self):
        response = connection.get_request_client().get(path=self.PATH_GET_MODELS)
        assert response.status_code == HTTPStatus.OK

        result = response.json()

        validate(instance=result, schema=self.GET_MODELS_SCHEMA)

        record = RedisUtils.get_models_key()
        assert record is not None

        assert record == result.get("data", {})
