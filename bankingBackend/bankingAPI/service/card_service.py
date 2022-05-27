import logging
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Union

from djangoProject.model.entity.card import Card


class CardService(ABC):
    @abstractmethod
    def add(self, card: Card):
        logging.debug('add method executed')

    @abstractmethod
    def refill(self, data: List[Union[str, Decimal]]):
        logging.debug('refill method executed')

    @abstractmethod
    def check_amount_of_cash(self, data: List[Union[str, Decimal]]):
        logging.debug('check_amount_of_cash method executed')

    @abstractmethod
    def transfer(self, data: List[Union[str, Decimal]]):
        logging.debug('transfer method executed')

    @abstractmethod
    def withdraw(self, data: List[Union[str, Decimal]]):
        logging.debug('withdraw method executed')
