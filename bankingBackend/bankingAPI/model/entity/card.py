import json
from decimal import Decimal


class Card:
    def __init__(self, card_number: str, pin: str, expiration_date: str):
        self._card_id: int = None
        self._card_number = card_number
        self._pin = pin
        self._expiration_date = expiration_date
        self._amount_of_cash: Decimal = None

    def get_card_id(self) -> int:
        return self._card_id

    def set_card_id(self, card_id: int) -> None:
        self._card_id = card_id

    def get_card_number(self) -> str:
        return self._card_number

    def set_card_number(self, card_number: str) -> None:
        self._card_number = card_number

    def get_pin(self) -> str:
        return self._pin

    def set_pin(self, pin: str) -> None:
        self._pin = pin

    def get_expiration_date(self) -> str:
        return self._expiration_date

    def set_expiration_date(self, expiration_date: str) -> None:
        self._expiration_date = expiration_date

    def get_amount_of_cash(self) -> Decimal:
        return self._amount_of_cash

    def set_amount_of_cash(self, amount_of_cash: Decimal) -> None:
        self._amount_of_cash = amount_of_cash

    def get_json_card(self) -> str:
        return json.dumps(self.__dict__)
