import PySimpleGUI as sg 
import Cliente

class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def tela_consulta(self):
        linha0 = [sg.Text("Digite o código ou o nome do cliente e clique em pesquisar:")]
        linha1 = [sg.Text("Nome:"), sg.InputText("", key="nome")]
        linha2 = [sg.Text("Código:"), sg.InputText("", key="codigo")]
        linha3 = [sg.Button("Consultar")]
        linha4 = [sg.Text("", size=(40,1), key="resultado")]
        
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()