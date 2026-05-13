from abc import ABC, abstractmethod


class DiscountStrategy(ABC):

    @abstractmethod
    def aplicar(self, preco, quantidade):
        pass