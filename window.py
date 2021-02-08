import PySimpleGUI as sg

class WindowBot:
    def __init__(self):
        layout = [
            [sg.Text("Canal:", size=(7, 0)), sg.Input(size=(15, 0))],
            [sg.Text("Dia:", size=(7, 0)), sg.Input(size=(15, 0))],
            [sg.Text("Horário:", size=(7, 0)), sg.Input(size=(15, 0,))],
            [sg.Button("OK",  size=(19, 0))]
        ]

        window = sg.Window("Bot CMSP").layout(layout)

        self.button, self.values = window.Read()

    def InitBot(self):
        canal = self.values[0]
        dia = self.values[1]
        horario = self.values[2]

        return canal
 
tela = WindowBot()
tela.InitBot()
