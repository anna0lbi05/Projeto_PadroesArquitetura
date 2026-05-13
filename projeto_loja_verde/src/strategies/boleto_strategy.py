from src.strategies.payment_strategy import PaymentStrategy


class BoletoPaymentStrategy(PaymentStrategy):

    def processar(self, pedido, valor):
        if valor < pedido.tot:
            return False

        print("Gerando boleto...")
        print("Boleto gerado!")

        return True