from src.repositories.pedido_repository import PedidoRepository

from src.services.pedido_service import PedidoService

from src.observers.notification_manager import NotificationManager
from src.observers.email_notifier import EmailNotifier
from src.observers.sms_notifier import SMSNotifier
from src.observers.corporate_notifier import CorporateNotifier


repository = PedidoRepository()

notification_manager = NotificationManager()

notification_manager.add_observer(
    EmailNotifier()
)

notification_manager.add_observer(
    SMSNotifier()
)

notification_manager.add_observer(
    CorporateNotifier()
)

service = PedidoService(
    repository,
    notification_manager
)