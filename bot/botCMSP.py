import pyautogui
import os
import PySimpleGUI as sg
import sched
import time
from datetime import date

sg.theme('DarkGrey12')

canais = [
    "cmsp-1ef-sp-p", "cmsp-2ef-sp-p", "cmsp-3ef-sp-p", 
    "cmsp-4ef-sp-p", "cmsp-5ef-sp-p", "cmsp-6ef-p", 
    "cmsp-7ef-p", "cmsp-8ef-p", "cmsp-9ef-p", 
    "cmsp-1em-p", "cmsp-2em-p", "cmsp-3em-p", 
    "treinamentosp01-p", "treinamentosp02-p"
]

layout = [
    # [sg.Text("Canal:", size=(8, 0)), sg.Input(size=(16, 0), key="canal")],
    [sg.Listbox(canais, size=(40, 10), key="canal")],
    [sg.Text("Dia:", size=(8, 0)), sg.Input(size=(31, 0), key="dia")],
    [sg.Text("Horário:", size=(8, 0)), sg.Input(size=(31, 0,), key="horario")],
    [sg.Button("OK", size=(10, 1))]
]

window = sg.Window("Bot CMSP", icon='references/iconcmsp.ico', element_justification='center').layout(layout)

event, values = window.read()

canal = str(values['canal'])
char_to_replace = {
    "[": '',
    "]": '',
    "'": ''
}

for key, value in char_to_replace.items():
    canal = canal.replace(key, value)

dia = values['dia']
horario = values['horario']

if event == 'OK':
    window.Hide()


def botCMSP():
    # print("Bot rodando...")
    os.startfile('C:/Program Files/IP.TV Studio HD 518/iptv.exe')
    time.sleep(1)

    iptvButton = pyautogui.locateCenterOnScreen('references/iptvbutton.png', confidence=0.8)
    pyautogui.click(iptvButton)

    iptvwindow = pyautogui.locateCenterOnScreen('references/iptvwindow.png', grayscale=True, confidence=0.8)

    k = 0
    while iptvwindow == None:
        iptvwindow = pyautogui.locateCenterOnScreen('references/iptvwindow.png', grayscale=True, confidence=0.8)
        k += 1 
        # print(iptvwindow, k)

        if ((iptvwindow) is not None):
        
            pyautogui.typewrite(canal)
            time.sleep(0.5)

            pyautogui.press('tab', presses=4)
            pyautogui.press('up')
            pyautogui.press('enter')

            iptvblackwindow = pyautogui.locateCenterOnScreen('references/iptvblackwindow.png', grayscale=True, confidence=0.8)

            i = 0
            while iptvblackwindow == None:
                iptvblackwindow = pyautogui.locateCenterOnScreen('references/iptvblackwindow.png', confidence=0.8)
                i += 1 
                # print(iptvblackwindow, i)

                if ((iptvblackwindow) is not None):

                    iptvUsers = pyautogui.locateCenterOnScreen('references/iptvusers.png', confidence=0.8)
                    pyautogui.click(iptvUsers)
                    time.sleep(0.3)

                    iptvsptransmit = pyautogui.locateCenterOnScreen('references/iptvsptransmit.png', confidence=0.8)
                    pyautogui.click(iptvsptransmit)
                    # pyautogui.keyDown('ctrl')
                    # pyautogui.press('v')
                    # pyautogui.keyUp('ctrl')
                    time.sleep(0.3)

                    playlistButton = pyautogui.locateCenterOnScreen('references/playlistbutton.png', confidence=0.8)
                    pyautogui.click(playlistButton)
                    time.sleep(0.3)

                    pyautogui.keyDown('win')
                    pyautogui.press('1')
                    pyautogui.keyUp('win')
                
                    
                    pyautogui.alert(text="Programação concluída com sucesso!")


scheduler = sched.scheduler(time.time, time.sleep)
# t = time.strptime("2021-02-"+dia+" "+horario+":00", '%Y-%m-%d %H:%M:%S')
t = time.strptime("21/02/"+dia+" "+horario, "%y/%m/%d %H:%M")
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, botCMSP, ())
scheduler.run()
            