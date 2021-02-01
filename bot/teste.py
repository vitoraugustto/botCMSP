import pyautogui

iptvwindow = pyautogui.locateCenterOnScreen('references/iptvwindow.png', confidence=0.7)

print(iptvwindow)