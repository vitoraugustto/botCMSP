import pyautogui
import os
import sched
import time
from datetime import date
import PySimpleGUI as sg

sg.theme('DarkGrey8')

canais = [
    "cmsp-1ef-sp-p", "cmsp-2ef-sp-p", "cmsp-3ef-sp-p", "cmsp-4ef-sp-p", "cmsp-5ef-sp-p", "cmsp-6ef-p", "cmsp-7ef-p", 
    "cmsp-8ef-p", "cmsp-9ef-p", "cmsp-1em-p", "cmsp-2em-p", "cmsp-3em-p"
]

layout = [
    # [sg.Text("Canal:", size=(8, 0)), sg.Input(size=(16, 0), key="canal")],
    [sg.Listbox(canais, select_mode='single', size=(40, 10), key="canal")],
    [sg.Text("Dia:", size=(8, 0)), sg.Input(size=(31, 0), key="dia")],
    [sg.Text("Horário:", size=(8, 0)), sg.Input(size=(31, 0,), key="horario")],
    [sg.Button("OK", size=(10, 1))]
]


window = sg.Window("Bot CMSP", icon='references/iconcmsp.ico', element_justification='center').layout(layout)

event, values = window.read()

canal = values['canal']
dia = values['dia']
horario = values['horario']


def botCMSP():
    os.startfile('C:/Windows/System32/notepad.exe')
    time.sleep(1)
    pyautogui.typewrite(canal)


scheduler = sched.scheduler(time.time, time.sleep)
t = time.strptime("2021-02-"+dia+" "+horario+":00", '%Y-%m-%d %H:%M:%S')
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, botCMSP, ())
scheduler.run()
            