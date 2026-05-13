from src.observers.observer import Observer


class CorporateNotifier(Observer):

    def update(self, mensagem):
        print(f"GERENTE CORPORATIVO: {mensagem}")
        