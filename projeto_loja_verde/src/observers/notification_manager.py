class NotificationManager:

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, mensagem):

        for observer in self.observers:
            observer.update(mensagem)