from src.strategies.discounts.discount_strategy import DiscountStrategy


class Discount10Strategy(DiscountStrategy):

    def aplicar(self, preco, quantidade):

        return preco * quantidade * 0.9