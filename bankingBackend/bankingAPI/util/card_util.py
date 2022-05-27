import logging
from abc import ABC, abstractmethod

from djangoProject.model.entity.card import Card


class CardUtil(ABC):
    @abstractmethod
    def is_exists(self, card: Card):
        logging.debug('is_exists method executed')

    @staticmethod
    @abstractmethod
    def check_length(pin: str, card_number: str):
        logging.debug('check_length method executed')
