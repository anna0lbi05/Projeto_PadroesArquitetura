from abc import ABC, abstractmethod


class CustomerStrategy(ABC):

    @abstractmethod
    def aplicar_desconto(self, total):
        pass