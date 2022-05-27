import logging
from decimal import Decimal
from typing import List, Union, Tuple, Any

from djangoProject.dao.card_dao import CardDao
from djangoProject.exception.card_exists_exception import CardExistsException
from djangoProject.exception.card_not_found_exception import CardNotFoundException
from djangoProject.exception.illegal_amount_exception import IllegalAmountException
from djangoProject.model.entity.card import Card
from djangoProject.service.card_service import CardService
from djangoProject.service.util.card_util import CardUtil


class CardServiceImpl(CardService):

    def __init__(self, card_util: CardUtil, card_dao: CardDao):
        super(CardService, self).__init__()
        self._card_util = card_util
        self._card_dao = card_dao

    def add(self, card: Card) -> None:
        try:
            self._card_util.check_length(card.get_pin(), card.get_card_number())

            self._card_util.is_exists(card)
        except TypeError or CardExistsException:
            logging.error('Card not valid')

        self._card_dao.save_card(card)

    def refill(self, data: List[Union[str, Decimal]]) -> None:
        card_number: str = data[0]
        pin: str = data[1]
        amount_of_cash: Decimal = data[2]

        self._card_util.check_length(pin, card_number)

        if amount_of_cash == 0:
            raise IllegalAmountException('amount of cash must be not 0 for refilling operation')

        check_card = self._card_dao.find_card_by_card_number_and_pin(card_number, pin)

        if check_card is None:
            raise CardNotFoundException('card with number {} not found'.format(card_number))

        self._card_dao.update_cards_amount(amount_of_cash, card_number)

    def check_amount_of_cash(self, data: List[Union[str, Decimal]]) -> Decimal:
        card_number: str = data[0]
        pin: str = data[1]

        self._card_util.check_length(pin, card_number)

        return self._card_dao.find_amount_of_cash_by_card_number_and_pin(card_number, pin)[0]

    def transfer(self, data: List[Union[str, Decimal]]) -> List[Tuple[Any, ...]]:
        card_number: str = data[0]
        pin: str = data[1]
        amount_of_cash_to_transfer: Decimal = data[2]
        participant_card_number: str = data[3]

        self._card_util.check_length(pin, card_number)

        return self._card_dao.transfer_cash_from_one_card_to_participant_card(card_number,
                                                                              pin,
                                                                              participant_card_number,
                                                                              amount_of_cash_to_transfer)

    def withdraw(self, data: List[Union[str, Decimal]]) -> Tuple[Any, ...]:
        card_number: str = data[0]
        pin: str = data[1]
        amount_of_cash_to_withdraw: Decimal = data[2]

        self._card_util.check_length(pin, card_number)

        return self._card_dao.withdraw_cash_from_card(amount_of_cash_to_withdraw,
                                                      card_number, pin)

