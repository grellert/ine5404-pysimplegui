import PySimpleGUI as sg

def calcularIMC(values):
    # processamento básico para garantir altura em cm
    alturaStr = values["altura"].replace(",","").replace(".","")
    peso = float(values["peso"])
    altura = float(alturaStr)/100
    imc = peso/(altura**2)
    return round(imc,2)

import PySimpleGUI as sg

linha0 = [sg.Text("Qual seu peso?")], sg.InputText("", key="peso"), sg.Text("Kg")]
linha1 = [sg.Text("Qual sua altura?"), sg.InputText("", key="altura"), sg.Text("cm")]
linha2 = [sg.Text("Seu IMC é"),sg.Text('', key="imc", size=(6,1))]
linha3 = [sg.Text('', size=(14,1)), sg.Button("Calcular IMC")]
container = [linha0, linha1, linha2, linha3]


# Janela principal
window = sg.Window("Calculadora de IMC", container,font=("Helvetica", 14))

# Loop de eventos
rodando = True
while rodando:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED:
        rodando = False
    elif event == 'Calcular IMC':
        imc = calcularIMC(values)
        window.Element('imc').Update(imc)

window.close()