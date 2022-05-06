import pyautogui
import time

def Desk1():
    pyautogui.hotkey('ctrl','num1')

def Sheet1():
    pyautogui.hotkey('ctrl','1')

def Down():
    pyautogui.press('down')

def Copy():
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)

def Sheet2():
    pyautogui.hotkey('ctrl','2')

def CommandBuscar():
    pyautogui.hotkey('ctrl','f')

def Capture():
    pyautogui.hotkey('ctrl', 'shift', 'print')
    time.sleep(1)
    pyautogui.mouseDown(x=715, y=504)
    pyautogui.mouseUp(x=1472, y=1010)
    time.sleep(1)

def Click():
    pyautogui.click(x=367, y=723)

def Desk6():
    pyautogui.hotkey('ctrl','num6')

def Paste():
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)

def Alinear():
    pyautogui.click(x=1714, y=200)

def Order():
    pyautogui.press('f8')
    pyautogui.click(x=869, y=663)
    pyautogui.write('Order: ', interval=0.15)

def Move():
    pyautogui.press('f1')

def Left():
    pyautogui.press('left')

def Right():
    pyautogui.press('right')

def Guardar():
    pyautogui.hotkey('ctrl','shift', 's')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)

def Delete():
    pyautogui.press('f1')
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
    time.sleep(1)

def Play():
    pyautogui.hotkey('ctrl','num4')
    time.sleep(1)
    pyautogui.click(x=1780, y=75)


# execution

Desk1()
Sheet1()
Down()
Copy()
Sheet2()
CommandBuscar()
Paste()
time.sleep(3)
Click()
Capture()
Desk6()
time.sleep(1)
Paste()
time.sleep(1)
Alinear()
time.sleep(1)
Order()
time.sleep(1)
Desk1()
time.sleep(1)
Sheet1()
time.sleep(1)
Left()
Copy()
Right()
Desk6()
time.sleep(1)
Paste()
time.sleep(1)
Move()
time.sleep(1)


Save = pyautogui.alert(text='Guardar?', title='Guardar!!!', button='OK')
if Save == 'OK':
        time.sleep(1)
        Guardar()
        time.sleep(2)
        Delete()

Play()