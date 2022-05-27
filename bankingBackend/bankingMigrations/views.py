import json
import logging

from decimal import Decimal

from dateutil import parser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from banking.JsonFactory import JsonFactory
from djangoProject.dao.impl.card_dao_impl import CardDaoImpl
from djangoProject.exception.exception_factory import ExceptionFactory
from djangoProject.model.entity.card import Card
from djangoProject.service.impl.card_service_impl import CardServiceImpl
from djangoProject.util.impl.card_util_impl import CardUtilImpl


CONTENT_TYPE_JSON={'Content-Type': 'application/json'}


@csrf_exempt
def add(request):
    if request.method != 'POST':
        return HttpResponse(ExceptionFactory.exception_builder('HTTP Method should be POST'), status=400, headers=CONTENT_TYPE_JSON)

    body = json.loads(request.body)
    print(body)
    card_dto: Card = Card(body['cardNumber'],
                          body['PIN'],
                          parser.parse(body['expirationDate']).strftime('%m-%y'))

    card_dao = CardDaoImpl()
    card_util = CardUtilImpl(card_dao)
    card_service = CardServiceImpl(card_util, card_dao)

    card_service.add(card_dto)

    return HttpResponse(status=204)


@csrf_exempt
def refill(request):
    logging.warning(request.content_type)
    if request.method != 'GET':
        return HttpResponse(ExceptionFactory.exception_builder('HTTP Method should be GET'), status=400, headers=CONTENT_TYPE_JSON)

    try:
        card_number: str = request.headers['cardNumber']
        pin: str = request.headers['PIN']
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)
        card_service.refill([card_number, pin, request.GET['amount']])

        return HttpResponse(status=204)
    except KeyError:
        return HttpResponse(ExceptionFactory.exception_builder('Permission denied. Please provide your card first'), status=403, headers=CONTENT_TYPE_JSON)


@csrf_exempt
def check_money(request):
    if request.method != 'GET':
        return HttpResponse(ExceptionFactory.exception_builder('HTTP Method should be GET'), status=400, headers=CONTENT_TYPE_JSON)

    try:
        card_number: str = request.headers['cardNumber']
        pin: str = request.headers['PIN']

        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        amount: Decimal = card_service.check_amount_of_cash([card_number, pin])

        return HttpResponse(JsonFactory.dto_builder('amount', str(amount)), status=200, headers=CONTENT_TYPE_JSON)
    except KeyError:
        return HttpResponse(ExceptionFactory.exception_builder('Permission denied. Please provide your card first'), status=403, headers=CONTENT_TYPE_JSON)


@csrf_exempt
def transfer(request):
    if request.method != 'POST':
        return HttpResponse(ExceptionFactory.exception_builder('HTTP Method should be POST'), status=400, headers=CONTENT_TYPE_JSON)

    try:
        card_number: str = request.headers['cardNumber']
        pin: str = request.headers['PIN']

        body = json.loads(request.body)

        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        updated_amounts = card_service.transfer([card_number, pin, body['amount'], body['cardToTransfer']])

        return HttpResponse(JsonFactory.dto_builder('updatedChecksum', str(updated_amounts)), headers=CONTENT_TYPE_JSON)
    except KeyError:
        return HttpResponse(ExceptionFactory.exception_builder('Permission denied. Please provide your card first'), status=403, headers=CONTENT_TYPE_JSON)


@csrf_exempt
def withdraw(request):
    if request.method != 'GET':
        return HttpResponse(ExceptionFactory.exception_builder('HTTP Method should be GET'), status=400, headers=CONTENT_TYPE_JSON)

    try:
        card_number: str = request.headers['cardNumber']
        pin: str = request.headers['PIN']

        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        withdraw_amount = card_service.withdraw([card_number, pin, Decimal(request.GET['withdrawCash'])])

        return HttpResponse(JsonFactory.dto_builder('amount', str(withdraw_amount)), status=200, headers=CONTENT_TYPE_JSON)
    except KeyError:
        return HttpResponse(ExceptionFactory.exception_builder('Permission denied. Please provide your card first'), status=403, headers=CONTENT_TYPE_JSON)
