from src.observers.observer import Observer


class SMSNotifier(Observer):

    def update(self, mensagem):
        print(f"SMS: {mensagem}")