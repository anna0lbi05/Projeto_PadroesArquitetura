from datetime import datetime

from src.repositories.pedido_repository import PedidoRepository
from src.factories.payment_factory import PaymentFactory
from src.observers.notification_manager import NotificationManager
from src.observers.email_notifier import EmailNotifier
from src.observers.sms_notifier import SMSNotifier
from src.observers.corporate_notifier import CorporateNotifier

class PedidoService:

    def __init__(self):
        self.repository = PedidoRepository()

        self.notification_manager = NotificationManager()

    def criar_pedido(self, cliente, itens, tipo_cliente):

        total = 0

        for item in itens:

            subtotal = item['p'] * item['q']

            if item['tipo'] == 'desc10':
                subtotal *= 0.9

            elif item['tipo'] == 'desc20':
                subtotal *= 0.8

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

        self._configurar_notificacoes(tipo_cliente)

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


    def _configurar_notificacoes(self, tipo_cliente):

        self.notification_manager.observers = []

        self.notification_manager.add_observer(
            EmailNotifier()
        )

        if tipo_cliente == 'vip':
            self.notification_manager.add_observer(
                SMSNotifier()
            )

        elif tipo_cliente == 'corporativo':
            self.notification_manager.add_observer(
                CorporateNotifier()
            )