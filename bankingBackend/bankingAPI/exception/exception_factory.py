import json


class ExceptionFactory:
    def __init__(self):
        pass

    @staticmethod
    def exception_builder(message: str) -> str:
        response_data: dict = {'message': message}

        return json.dumps(response_data)
