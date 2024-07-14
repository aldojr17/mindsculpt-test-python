from http import HTTPStatus

from parameterized import parameterized
from jsonschema import validate

import connection
from connection.db.db import DBUtils
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
        body = self.generate_body()
        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.CREATED

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.GENERATION_SCHEMA)

        data = result.get("data")

        record = DBUtils.get_image_generation_by_id(data.get("uuid", ""))
        assert record is not None

        assert record.get("id") == data.get("uuid")
        assert record.get("url") == data.get("image_url")
        assert record.get("censored") == data.get("censored")

    @parameterized.expand(
        [
            MindsculptBase.RATIO_1_1,
            MindsculptBase.RATIO_2_3,
            MindsculptBase.RATIO_3_2,
            MindsculptBase.RATIO_9_16,
            MindsculptBase.RATIO_16_9,
        ]
    )
    def test_generate_image_with_different_ratio(self, ratio):
        body = self.generate_body(ratio)
        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.CREATED

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.GENERATION_SCHEMA)

        data = result.get("data")

        record = DBUtils.get_image_generation_by_id(data.get("uuid", ""))
        assert record is not None

        assert record.get("id") == data.get("uuid")
        assert record.get("url") == data.get("image_url")
        assert record.get("censored") == data.get("censored")

    def test_generate_image_with_required_field_only(self):
        body = {
            "query": self.generate_query()
        }
        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.CREATED

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.GENERATION_SCHEMA)

        data = result.get("data")

        record = DBUtils.get_image_generation_by_id(data.get("uuid", ""))
        assert record is not None

        assert record.get("id") == data.get("uuid")
        assert record.get("url") == data.get("image_url")
        assert record.get("censored") == data.get("censored")

    def test_generate_image_with_non_english_words(self):
        body = self.generate_body("冰茶")
        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.CREATED

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.GENERATION_SCHEMA)

        data = result.get("data")

        record = DBUtils.get_image_generation_by_id(data.get("uuid", ""))
        assert record is not None

        assert record.get("id") == data.get("uuid")
        assert record.get("url") == data.get("image_url")
        assert record.get("censored") == data.get("censored")

    def test_generate_image_with_null_value_for_optional_field(self):
        body = self.generate_body()
        body = {key: value if key == "query" else None for key, value in body.items()}

        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.CREATED

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.GENERATION_SCHEMA)

        data = result.get("data")

        record = DBUtils.get_image_generation_by_id(data.get("uuid", ""))
        assert record is not None

        assert record.get("id") == data.get("uuid")
        assert record.get("url") == data.get("image_url")
        assert record.get("censored") == data.get("censored")

    def test_generate_image_with_more_than_maximum_query_length(self):
        body = self.generate_body("a"*1001)
        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.BAD_REQUEST_SCHEMA)

    def test_generate_image_without_required_field(self):
        body = self.generate_body()
        del body["query"]

        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.BAD_REQUEST_SCHEMA)

    @parameterized.expand(
        [
            ("width", "1280"),
            ("height", "1280"),
            ("model_id", "4"),
            ("query", 1280),
            ("negative_prompt_unclip", 1280),
        ])
    def test_generate_image_with_invalid_data_types(self, field, value):
        body = self.generate_body()
        body[field] = value

        response = connection.get_request_client().post(path=self.PATH_GENERATE, body=body)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        result = response.json()

        validate(instance=result, schema=MindsculptSchema.BAD_REQUEST_SCHEMA)
