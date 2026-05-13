from src.factories.payment_factory import PaymentFactory
from src.factories.customer_factory import CustomerFactory
from src.factories.discount_factory import DiscountFactory

from src.strategies.cartao_strategy import CartaoPaymentStrategy
from src.strategies.pix_strategy import PixPaymentStrategy
from src.strategies.boleto_strategy import BoletoPaymentStrategy

from src.strategies.customers.normal_customer import NormalCustomer
from src.strategies.customers.vip_customer import VipCustomer
from src.strategies.customers.corporate_customer import CorporateCustomer

from src.strategies.discounts.normal_discount import NormalDiscount
from src.strategies.discounts.discount_10 import Discount10Strategy
from src.strategies.discounts.discount_20 import Discount20Strategy

import pytest


def test_payment_factory_cria_cartao():
    strategy = PaymentFactory.criar('cartao')
    assert isinstance(strategy, CartaoPaymentStrategy)


def test_payment_factory_cria_pix():
    strategy = PaymentFactory.criar('pix')
    assert isinstance(strategy, PixPaymentStrategy)


def test_payment_factory_cria_boleto():
    strategy = PaymentFactory.criar('boleto')
    assert isinstance(strategy, BoletoPaymentStrategy)


def test_payment_factory_lanca_erro_metodo_invalido():
    with pytest.raises(ValueError):
        PaymentFactory.criar('invalido')


def test_customer_factory_cria_cliente_vip():
    customer = CustomerFactory.criar('vip')
    assert isinstance(customer, VipCustomer)


def test_customer_factory_cria_cliente_corporativo():
    customer = CustomerFactory.criar('corporativo')
    assert isinstance(customer, CorporateCustomer)


def test_customer_factory_cria_cliente_normal():
    customer = CustomerFactory.criar('normal')
    assert isinstance(customer, NormalCustomer)


def test_discount_factory_cria_discount_10():
    discount = DiscountFactory.criar('desc10')
    assert isinstance(discount, Discount10Strategy)


def test_discount_factory_cria_discount_20():
    discount = DiscountFactory.criar('desc20')
    assert isinstance(discount, Discount20Strategy)


def test_discount_factory_cria_normal_discount():
    discount = DiscountFactory.criar('normal')
    assert isinstance(discount, NormalDiscount)