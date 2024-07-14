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

    GENERATION_SCHEMA = {
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "uuid": {
                        "type": "string"
                    },
                    "status": {
                        "type": "string"
                    },
                    "image_url": {
                        "type": "string"
                    },
                    "censored": {
                        "type": "boolean"
                    }
                },
                "required": ["uuid", "status", "image_url", "censored"]
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

    BAD_REQUEST_SCHEMA = {
        "type": "object",
        "properties": {
            "error": {
                "type": "null"
            },
            "is_success": {
                "type": "boolean"
            },
            "message": {
                "type": "string"
            },
        },
        "required": ["error", "is_success", "message"],
    }
