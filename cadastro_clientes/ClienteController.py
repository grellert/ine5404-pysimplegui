from ClienteView import ClienteView
from ClienteDAO import ClienteDAO
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clienteDAO = ClienteDAO()

    def inicia(self):
        container = self.__telaCliente.tela_consulta()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()
            print(event, values)
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Consultar':
                if values["codigo"] != '':
                    codigo = int(values["codigo"])
                    try:
                        resultado = self.__clienteDAO.get(codigo)
                    except:
                        resultado = "Não encontrado"

                elif values["nome"] != '':
                    try:
                        codigo = self.__clienteDAO.find(values["nome"])
                        resultado = self.__clienteDAO.get(codigo)
                    except KeyError:
                        resultado = "Não encontrado"
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()