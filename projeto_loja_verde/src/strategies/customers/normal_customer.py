from src.strategies.customers.customer_strategy import (
    CustomerStrategy
)


class NormalCustomer(CustomerStrategy):

    def aplicar_desconto(self, total):

        return total