from src.observers.observer import Observer


class EmailNotifier(Observer):

    def update(self, mensagem):
        print(f"EMAIL: {mensagem}")