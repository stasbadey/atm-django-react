from typing import Tuple

from djangoProject.dao.card_dao import CardDao
from djangoProject.exception.card_exists_exception import CardExistsException
from djangoProject.model.entity.card import Card
from djangoProject.service.util.card_util import CardUtil


class CardUtilImpl(CardUtil):
    def __init__(self, card_dao: CardDao):
        self._card_dao = card_dao

    def is_exists(self, card: Card) -> None:
        cards: Tuple[Card] = self._card_dao.find_all_card()

        for counter in range(len(cards)):
            if card.get_card_number() == cards[counter]:
                raise CardExistsException('card with id {} already exists'.format(card.get_card_id()))

    @staticmethod
    def check_length(pin: str, card_number: str) -> None:
        if any((len(pin) != 4, len(card_number) != 16)):
            raise TypeError("length of pin should be 4 and length of card number 16")
