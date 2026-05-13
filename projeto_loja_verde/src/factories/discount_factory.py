from src.strategies.discounts.normal_discount import NormalDiscount

from src.strategies.discounts.discount_10 import (
    Discount10Strategy
)

from src.strategies.discounts.discount_20 import (
    Discount20Strategy
)


class DiscountFactory:

    @staticmethod
    def criar(tipo):

        if tipo == 'desc10':
            return Discount10Strategy()

        elif tipo == 'desc20':
            return Discount20Strategy()

        return NormalDiscount()