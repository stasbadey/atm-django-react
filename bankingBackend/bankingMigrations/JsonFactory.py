import json


class JsonFactory:
    def __init__(self):
        pass

    @staticmethod
    def dto_builder(json_message: str, model: str) -> str:
        return json.dumps({json_message: model})
