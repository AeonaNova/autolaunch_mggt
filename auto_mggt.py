import pyautogui
import time
import os
import pyperclip
import win32api
import win32gui


with open('entry.txt', 'r', encoding='ascii') as file:
     entrys = file.read().split(',')
     l, p = str(entrys[1]), str(entrys[0])


time.sleep(4)


os.startfile ("mggtRecon\mggtRecon.exe")


time.sleep(4)


try:
     cords = pyautogui.locateCenterOnScreen('L.png')
     cords_y = cords[1]
except Exception as ex:
     print(ex)
try:
     cords = pyautogui.locateCenterOnScreen('L2.png')
     cords_y = cords[1]
except Exception as ex:
     print(ex)
try:     
     if cords_y < 515:
          pyautogui.click(cords)
          pyperclip.copy(l)
          pyautogui.hotkey("ctrl", "v")
          pyperclip.copy('')
except Exception as ex:
     print(ex)
     
try:     
     cords = pyautogui.Point(x=958, y=505)
     pyautogui.click(cords)
     pyperclip.copy(l)
     pyautogui.hotkey("ctrl", "v")
     pyperclip.copy('')
except Exception as ex:
     print(ex)
     
try:
     P = pyautogui.locateCenterOnScreen('P.png')
     pyautogui.click(P)
     pyperclip.copy(p)
     pyautogui.hotkey("ctrl", "v")
     pyperclip.copy('')
except Exception as ex:
     print(ex)

OK = pyautogui.locateOnScreen('OK.png')
ok_button_center = pyautogui.center(OK)
pyautogui.click(ok_button_center)

