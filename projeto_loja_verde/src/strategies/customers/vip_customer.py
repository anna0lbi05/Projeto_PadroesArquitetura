from src.strategies.customers.customer_strategy import (
    CustomerStrategy
)


class VipCustomer(CustomerStrategy):

    def aplicar_desconto(self, total):

        return total * 0.95
    