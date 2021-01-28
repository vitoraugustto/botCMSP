import pyautogui
import os
import sched
import time
from datetime import date

print('Formato do horário: "HH:MM"')

dia = input('Digite o dia: ')
horario = input('Digite o horário: ')

def botCMSP():
    canal = input('Digite o canal: ')
    
    if canal:
        os.startfile('C:\Program Files\IP.TV Studio HD 518\iptv.exe')
        time.sleep(3)

        iptvButton = pyautogui.locateCenterOnScreen('references/iptvbutton.png')
        pyautogui.click(iptvButton)
        time.sleep(6)

        pyautogui.typewrite(canal)
        time.sleep(6)

        pyautogui.press('tab')
        pyautogui.press('tab') 
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('up')
        pyautogui.press('enter')


scheduler = sched.scheduler(time.time, time.sleep)
t = time.strptime('2021-01-'+dia+' '+horario+':00', '%Y-%m-%d %H:%M:%S')
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, botCMSP, ())
scheduler.run()