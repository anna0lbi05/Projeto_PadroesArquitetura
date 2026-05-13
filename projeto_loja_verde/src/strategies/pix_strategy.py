from src.strategies.payment_strategy import PaymentStrategy


class PixPaymentStrategy(PaymentStrategy):

    def processar(self, pedido, valor):
        if valor < pedido.tot:
            return False

        print("Gerando QR Code PIX...")
        print("PIX recebido!")

        return True