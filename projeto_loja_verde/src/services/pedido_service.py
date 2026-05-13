from datetime import datetime

from src.factories.discount_factory import DiscountFactory
from src.factories.payment_factory import PaymentFactory

class PedidoService:

    def __init__(
        self,
        repository,
        notification_manager
    ):

        self.repository = repository
        self.notification_manager = notification_manager

    def criar_pedido(self, cliente, itens, tipo_cliente):

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

        if tipo_cliente == 'vip':
            total *= 0.95

        elif tipo_cliente == 'corporativo':
            total *= 0.90

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

    def buscar_pedido(self, pedido_id):
        return self.repository.buscar_por_id(pedido_id)

    def atualizar_status(self, pedido_id, status):
        self.repository.atualizar_status(pedido_id, status)

    def processar_pagamento(self, pedido_id, metodo, valor):

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

    def listar_pedidos(self):
        return self.repository.listar_todos()

    def close(self):
        self.repository.close()