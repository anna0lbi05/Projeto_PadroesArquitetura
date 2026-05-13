from src.strategies.customers.normal_customer import (
    NormalCustomer
)

from src.strategies.customers.vip_customer import (
    VipCustomer
)

from src.strategies.customers.corporate_customer import (
    CorporateCustomer
)


class CustomerFactory:

    @staticmethod
    def criar(tipo):

        if tipo == 'vip':
            return VipCustomer()

        elif tipo == 'corporativo':
            return CorporateCustomer()

        return NormalCustomer()