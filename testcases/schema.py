class MindsculptSchema:
    GET_MODELS_SCHEMA = {
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "version": {
                        "type": "number"
                    },
                    "type": {
                        "type": "string"
                    }
                },
                "required": ["id", "name", "version", "type"]
            },
            "is_success": {
                "type": "boolean"
            },
            "message": {
                "type": "string"
            },
        },
        "required": ["data", "is_success", "message"],
    }
