import pyautogui
import os
import sched
import time
from datetime import date

print("#########################################")
print("#########################################")
print("#               CMSP BOT                #")
print("#########################################")
print("#########################################")

print("_________________________________________")
dia = input("Digite o dia: ")
print("_________________________________________")

print("Formato do horário: 'HH:MM'")

horario = input("Digite o horário: ")
print("_________________________________________")

def botCMSP():
    print("Bot rodando...")
    
    os.startfile('C:\Program Files\IP.TV Studio HD 518\iptv.exe')
    time.sleep(1)

    iptvButton = pyautogui.locateCenterOnScreen('references/iptvbutton.png')
    pyautogui.click(iptvButton)
    time.sleep(3)

    iptvwindow = pyautogui.locateCenterOnScreen('references/iptvbutton.png', confidence=0.7)

    if not (iptvwindow):
        
        pyautogui.typewrite('treinamento')
        time.sleep(0.5)

        pyautogui.press('tab', presses=4)
        pyautogui.press('up')
        pyautogui.press('enter')
        time.sleep(3)

        iptvUsers = pyautogui.locateCenterOnScreen('references/iptvusers.png', confidence=0.8)
        pyautogui.click(iptvUsers)
        time.sleep(3)

        iptvsptransmit = pyautogui.locateCenterOnScreen('references/iptvsptransmit.png', confidence=0.8)
        pyautogui.click(iptvsptransmit)
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        time.sleep(3)

        playlistButton = pyautogui.locateCenterOnScreen('references/playlistbutton.png', confidence=0.8)
        pyautogui.click(playlistButton)
        time.sleep(3)

        pyautogui.keyDown('win')
        pyautogui.press('1')
        pyautogui.keyUp('win')
        
        # sairButton = pyautogui.locateCenterOnScreen('references/sairButton.png')
        # pyautogui.click(sairButton)
        # time.sleep(1)
        
        print("Programação concluída com sucesso! ft. Vitão, Agnaldão and Betão.")
        pyautogui.alert(text="Programação concluída com sucesso! ft. Vitão, Agnaldão and Betão.")

scheduler = sched.scheduler(time.time, time.sleep)
t = time.strptime("2021-02-"+dia+" "+horario+":00", '%Y-%m-%d %H:%M:%S')
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, botCMSP, ())
scheduler.run()
