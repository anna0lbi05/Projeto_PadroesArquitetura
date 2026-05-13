from abc import ABC, abstractmethod


class RepositoryInterface(ABC):

    @abstractmethod
    def salvar(self, **kwargs):
        pass

    @abstractmethod
    def buscar_por_id(self, pedido_id):
        pass

    @abstractmethod
    def atualizar_status(self, pedido_id, status):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def close(self):
        pass