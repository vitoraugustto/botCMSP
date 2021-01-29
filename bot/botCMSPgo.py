import pyautogui
import os
import sched
import time
from datetime import date

print("Formato do horário: 'HH:MM'")

dia = input("Digite o dia: ")
horario = input("Digite o horário: ")

def botCMSP():
    
    os.startfile('C:\Program Files\IP.TV Studio HD 518\iptv.exe')
    time.sleep(3)

    iptvButton = pyautogui.locateCenterOnScreen('references/iptvbutton.png')
    pyautogui.click(iptvButton)
    time.sleep(3)

    pyautogui.typewrite('cmsp-7ef-p')
    time.sleep(3)

    pyautogui.press('tab', presses=4)
    pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(3)

    iptvUsers = pyautogui.locateCenterOnScreen('references/iptvusers.png', confidence=0.8)
    pyautogui.click(iptvUsers)
    time.sleep(3)

    iptvsptransmit = pyautogui.locateCenterOnScreen('references/iptvsptransmit1.png', confidence=0.8)
    pyautogui.click(iptvsptransmit)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(3)

    playlistButton = pyautogui.locateCenterOnScreen('references/playlistbutton.png', confidence=0.8)
    pyautogui.click(playlistButton)
    time.sleep(3)

    minimizarVMix = pyautogui.locateCenterOnScreen('references/minimizarVMix.png', confidence=0.8)
    pyautogui.click(minimizarVMix)
    time.sleep(1)
    '''
    sairButton = pyautogui.locateCenterOnScreen('references/sairButton.png')
    pyautogui.click(sairButton)
    time.sleep(1)
    '''

    pyautogui.alert(text="Programação concluída com sucesso! ft. Agnaldão, Vitão, Betão.")

scheduler = sched.scheduler(time.time, time.sleep)
t = time.strptime("2021-01-"+dia+" "+horario+":00", '%Y-%m-%d %H:%M:%S')
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, botCMSP, ())
scheduler.run()
