from src.strategies.discounts.discount_strategy import DiscountStrategy


class NormalDiscount(DiscountStrategy):

    def aplicar(self, preco, quantidade):

        return preco * quantidade