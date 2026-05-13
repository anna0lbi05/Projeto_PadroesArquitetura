from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def processar(self, pedido, valor):
        pass