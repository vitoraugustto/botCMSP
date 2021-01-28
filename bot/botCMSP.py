import pyautogui
import os
import sched
import time
from datetime import date

print('Formato do horário: DD HH:MM')
horario = input('Digite o horário: ')

def botCMSP():
    canal = input('Digite o canal: ')
    
    if canal:
        os.startfile('C:\Program Files\IP.TV Studio HD 518\iptv.exe')
        time.sleep(3)

        pyautogui.click(x= 677, y=534)
        time.sleep(3)

        pyautogui.typewrite(canal)
        time.sleep(3)

        pyautogui.press('tab')
        pyautogui.press('tab') 
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('up')
        pyautogui.press('enter')


scheduler = sched.scheduler(time.time, time.sleep)
t = time.strptime('2021-01-'+horario+':00', '%Y-%m-%d %H:%M:%S')
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, botCMSP, ())
scheduler.run()