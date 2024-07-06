from http import HTTPStatus

from jsonschema import validate

import connection
from connection.redis.redis import RedisUtils
from testcases.base import MindsculptBase
from testcases.schema import MindsculptSchema


class TestMindsculpt(MindsculptBase):

    def test_get_models(self):
        response = connection.get_request_client().get(path=self.PATH_GET_MODELS)
        assert response.status_code == HTTPStatus.OK

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.GET_MODELS_SCHEMA)

        record = RedisUtils.get_models_key()
        assert record is not None

        assert record == result.get("data", {})

    def test_generate_image(self):
        body = self.generate_body("football player")
        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.CREATED
