from DAO import DAO
from Cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (cliente is not None) and (isinstance(cliente.codigo, int)) and (isinstance(cliente, Cliente)):
            super().add(cliente.codigo, cliente)
   
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def find(self, nome: str):
        for chave, cliente in super().get_all():
            if cliente.nome == nome:
                return chave
        raise KeyError

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)