from Cliente import Cliente
from ClienteDAO import ClienteDAO
from ClienteController import ClienteController

c1 = Cliente(1, "Mateus")
c2 = Cliente(2, "Fulana")
c3 = Cliente(3, "Ciclano")

dao = ClienteDAO()

dao.add(c1)
dao.add(c2)
dao.add(c3)

control = ClienteController()

control.inicia()
