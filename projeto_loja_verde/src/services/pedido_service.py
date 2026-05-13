from datetime import datetime

from src.factories.discount_factory import DiscountFactory
from src.factories.payment_factory import PaymentFactory
from src.factories.customer_factory import CustomerFactory
from src.interfaces.repository_interface import (
    RepositoryInterface
)

from src.observers.notification_manager import (
    NotificationManager
)

class PedidoService:

    def __init__(
        self,
        repository: RepositoryInterface,
        notification_manager: NotificationManager
    ):

        self.repository = repository
        self.notification_manager = notification_manager

    def criar_pedido(
        self,
        cliente: str,
        itens: list,
        tipo_cliente: str
    ) -> int:

        total = 0

        for item in itens:

            strategy = DiscountFactory.criar(
                item['tipo']
            )

            subtotal = strategy.aplicar(
                item['p'],
                item['q']
            )

            total += subtotal

        customer_strategy = CustomerFactory.criar(tipo_cliente)
        total = customer_strategy.aplicar_desconto(total)

        pedido_id = self.repository.salvar(
            cli=cliente,
            itens=itens,
            tot=total,
            st='pendente',
            dt=str(datetime.now()),
            tp=tipo_cliente
        )

        self.notification_manager.notify(
            f"Pedido criado para {cliente}"
        )

        return pedido_id

    def buscar_pedido(self, pedido_id: int):
        return self.repository.buscar_por_id(pedido_id)

    def atualizar_status(
        self,
        pedido_id: int,
        status: str
    ):
        self.repository.atualizar_status(pedido_id, status)

    def processar_pagamento(
        self,
        pedido_id: int,
        metodo: str,
        valor: float
    ):

        pedido = self.repository.buscar_por_id(pedido_id)

        if not pedido:
            return False

        strategy = PaymentFactory.criar(metodo)

        aprovado = strategy.processar(pedido, valor)

        if aprovado and metodo in ['cartao', 'pix']:

            self.repository.atualizar_status(
                pedido_id,
                'aprovado'
            )

        return aprovado

    def listar_pedidos(self) -> list:
        return self.repository.listar_todos()

    def close(self) -> None:
        self.repository.close()