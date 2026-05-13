from src.strategies.payment_strategy import PaymentStrategy


class CartaoPaymentStrategy(PaymentStrategy):

    def processar(self, pedido, valor):
        if valor < pedido.tot:
            return False

        print("Processando pagamento com cartao...")
        print("Cartao validado!")

        return True