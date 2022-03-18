import pyautogui
import time

class ClickMisil():

    def Deskt1():
        pyautogui.hotkey('ctrl','num1')

    def Down():
        pyautogui.press('down')

    def Tab1():
        pyautogui.hotkey('ctrl','1')

    def Tab2():
        pyautogui.hotkey('ctrl','2')

    def  Copy():
        pyautogui.hotkey('ctrl','c')

    def ComandoBuscar():
        pyautogui.hotkey('ctrl','f')

    def Paste():
        pyautogui.hotkey('ctrl','v')

    def Back():
        pyautogui.click(x=24, y=49)


    def PasteGuia():
        pyautogui.doubleClick(x=796, y=134)
        Paste()
        pyautogui.press('enter')

    def CopyOrder():
        pyautogui.hotkey('ctrl','left')
        pyautogui.hotkey('ctrl','c')

    def Detail():
        pyautogui.click(x=98, y=455)

    def Declaration():
        pyautogui.click(x=695, y=273)
        time.sleep(1)
        pyautogui.click(x=700, y=374)

    def Save():
        pyautogui.click(x=1559, y=898)
        time.sleep(1)
        Paste()
        pyautogui.press('enter')




    Deskt1()
    time.sleep(1)

    Tab1()
    time.sleep(1)

    Down()
    Copy()
    time.sleep(1)

    Tab2()
    time.sleep(1)

    PasteGuia()
    time.sleep(12)

    Tab1()
    time.sleep(1)

    CopyOrder()

    Tab2()
    time.sleep(1)

    Detail()
    time.sleep(2)

    Declaration()
    time.sleep(8)

    Save()





