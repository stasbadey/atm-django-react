import logging
from decimal import Decimal
from typing import Union, List, Tuple, Any

import psycopg2 as psycopg2

from djangoProject.dao.card_dao import CardDao
from djangoProject.model.entity.card import Card


class CardDaoImpl(CardDao):
    def __init__(self):
        super(CardDao, self).__init__()
        pass

    @staticmethod
    def _open_database_connection() -> Union[Any, Any]:
        try:
            postgres_connection = psycopg2.connect("dbname='card_db' "
                                                   "user='postgres' "
                                                   "host='cryptostgres' "
                                                   "port='5432' "
                                                   "password='postgres'")
        except(Exception, ConnectionError) as error:
            logging.error('Exception occurred: {}'.format(error))

        return postgres_connection

    def find_all_card(self) -> List[Tuple[Any, ...]]:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
        SELECT * FROM card
        '''

        cursor.execute(query)
        cards = cursor.fetchall()

        cursor.close()
        postgres_connection.close()

        return cards

    def save_card(self, card: Card) -> None:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
        INSERT INTO card(card_number, expiration_date, pin) 
        VALUES (%s, %s, %s)
        '''

        params_to_insert = (card.get_card_number(), card.get_expiration_date(), card.get_pin())

        cursor.execute(query, params_to_insert)

        postgres_connection.commit()

        cursor.close()
        postgres_connection.close()

    def find_card_by_card_number_and_pin(self, card_number: str, pin: str) -> Card:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
                SELECT * FROM card WHERE card_number = %s AND pin = %s
                '''

        params_to_select = (card_number, pin)

        cursor.execute(query, params_to_select)
        card = cursor.fetchone()

        cursor.close()
        postgres_connection.close()

        return card

    def update_cards_amount(self, amount_of_cash: Decimal, card_number: str) -> None:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
        UPDATE card SET amount_of_cash = %s WHERE card_number = %s
        '''

        params_to_update = (amount_of_cash, card_number)

        cursor.execute(query, params_to_update)

        postgres_connection.commit()

        cursor.close()
        postgres_connection.close()

    def find_amount_of_cash_by_card_number_and_pin(self, card_number: str, pin: str) -> Decimal:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
        SELECT amount_of_cash FROM card WHERE card_number = %s AND pin = %s
        '''

        params_to_select = (card_number, pin)

        cursor.execute(query, params_to_select)
        amount_of_cash = cursor.fetchone()

        cursor.close()
        postgres_connection.close()

        return amount_of_cash

    def transfer_cash_from_one_card_to_participant_card(self,
                                                        card_number: str,
                                                        pin: str,
                                                        participant_card_number: str,
                                                        amount_of_cash_to_transfer: Decimal) -> List[Tuple[Any, ...]]:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''WITH 
        transfer_card AS (UPDATE card SET amount_of_cash = (amount_of_cash - %s) 
        WHERE card_number = %s AND pin = %s AND amount_of_cash >= %s RETURNING amount_of_cash),
        updated_participant_card AS (UPDATE card SET amount_of_cash = CASE WHEN 
        (SELECT amount_of_cash FROM transfer_card) IS NOT NULL THEN (amount_of_cash + %s) ELSE amount_of_cash END 
        WHERE card_number = %s RETURNING amount_of_cash)
        SELECT * FROM transfer_card, updated_participant_card;
        '''

        params_to_update = (amount_of_cash_to_transfer, card_number, pin,
                            amount_of_cash_to_transfer, amount_of_cash_to_transfer, participant_card_number)

        cursor.execute(query, params_to_update)
        cards = cursor.fetchall()

        postgres_connection.commit()

        cursor.close()
        postgres_connection.close()

        return cards

    def withdraw_cash_from_card(self, amount_of_cash_to_withdraw: Decimal, card_number: str, pin: str) -> Decimal:
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
        WITH 
        withdraw_card AS (UPDATE card SET amount_of_cash = (amount_of_cash - %s) 
        WHERE amount_of_cash >= %s AND card_number = %s AND pin = %s
        RETURNING amount_of_cash)
        SELECT * FROM withdraw_card
        '''

        params_to_update = (amount_of_cash_to_withdraw,
                            amount_of_cash_to_withdraw, card_number, pin)

        cursor.execute(query, params_to_update)
        remainder = cursor.fetchone()

        postgres_connection.commit()

        cursor.close()
        postgres_connection.close()

        return remainder[0]
