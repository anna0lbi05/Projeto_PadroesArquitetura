from src.observers.email_notifier import EmailNotifier
from src.observers.sms_notifier import SMSNotifier
from src.observers.corporate_notifier import CorporateNotifier
from src.observers.notification_manager import NotificationManager


def test_email_notifier_update():
    notifier = EmailNotifier()
    assert notifier.update("Pedido aprovado") is None


def test_sms_notifier_update():
    notifier = SMSNotifier()
    assert notifier.update("Pedido enviado") is None


def test_corporate_notifier_update():
    notifier = CorporateNotifier()
    assert notifier.update("Pedido corporativo") is None


def test_notification_manager_notifica_observers():
    manager = NotificationManager()

    email = EmailNotifier()
    sms = SMSNotifier()

    manager.add_observer(email)
    manager.add_observer(sms)

    manager.notify("Novo pedido")