from src.strategies.cartao_strategy import CartaoPaymentStrategy
from src.strategies.pix_strategy import PixPaymentStrategy
from src.strategies.boleto_strategy import BoletoPaymentStrategy


class PaymentFactory:

    @staticmethod
    def criar(metodo_pagamento):

        strategies = {
            'cartao': CartaoPaymentStrategy(),
            'pix': PixPaymentStrategy(),
            'boleto': BoletoPaymentStrategy()
        }

        strategy = strategies.get(metodo_pagamento)

        if not strategy:
            raise ValueError('Metodo de pagamento invalido')

        return strategy