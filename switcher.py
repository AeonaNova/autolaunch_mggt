import win32api
import win32gui
import os

def setCyrillicLayout():
    """
    switch keyboard keys to cyrillic
    """
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04190419)
    return(result)

def setEngLayout():
    """
    switch keyboard keys to english
    """
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04090409)
    return(result)

setEngLayout()
print("switched")

os.system("start cmd /c python auto_mggt.py")
