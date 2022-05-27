import logging
from abc import ABC, abstractmethod
from decimal import Decimal


from djangoProject.model.entity.card import Card


class CardDao(ABC):

    @abstractmethod
    def find_all_card(self):
        logging.debug('find_all_card method executed')

    @abstractmethod
    def save_card(self, card: Card):
        logging.debug('save_card method executed')

    @abstractmethod
    def find_card_by_card_number_and_pin(self, card_number: str, pin: str):
        logging.debug('find_card_by_card_number_and_pin method executed')

    @abstractmethod
    def update_cards_amount(self, amount_of_cash: Decimal, card_number: str):
        logging.debug('update_cards_amount method executed')

    @abstractmethod
    def find_amount_of_cash_by_card_number_and_pin(self, card_number: str, pin: str):
        logging.debug('find_amount_of_cash_by_card_number_and_pin method executed')

    @abstractmethod
    def transfer_cash_from_one_card_to_participant_card(self,
                                                        card_number: str,
                                                        pin: str,
                                                        participant_card_number: str,
                                                        amount_of_cash_to_transfer: Decimal):
        logging.debug('transfer_cash_from_one_card_to_participant_card method executed')

    @abstractmethod
    def withdraw_cash_from_card(self, amount_of_cash_to_withdraw: Decimal, card_number: str, pin: str):
        logging.debug('withdraw_cash_from_card method executed')
