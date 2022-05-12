
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
    pyautogui.mouseDown(x=733, y=460)
    pyautogui.mouseUp(x=1433, y=986)
    time.sleep(1)

def Click():
    pyautogui.click(x=367, y=723)

def Desk6():
    pyautogui.hotkey('ctrl','num6')

def Paste():
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)

def AlinearVertical():
    pyautogui.click(x=1714, y=200)

def AlinearHorizontal():
    pyautogui.click(x=1709, y=231)

def Order():
    pyautogui.press('f8')
    pyautogui.click(x=822, y=585)
    pyautogui.write('Order: ', interval=0.15)

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
time.sleep(2)
Click()
MensajeCapturar = pyautogui.alert(text='Presiona OK despues de capturar', title='Capturar!!!', button='OK')
if MensajeCapturar == 'OK':
        Desk6()
        Paste()
        AlinearVertical()
        AlinearHorizontal()
        Desk1()
else:
    print("No encontrado")

Encabezado = pyautogui.alert(text='Presiona OK despues de capturar el encabeza', title='Encabezado!!!', button='OK')
if Encabezado == 'OK':
        Desk6()
        Paste()
        AlinearVertical()

PegarOrder = pyautogui.alert(text='Alinear ambos captures', title='Alinear!!!', button='OK')
if PegarOrder == 'OK':
        time.sleep(1)       
        Order()
        Desk1()
        Sheet1()
        Left()
        Copy()
        Right()
        Desk6()
        Paste()

Save = pyautogui.alert(text='Guardar?', title='Guardar!!!', button='OK')
if Save == 'OK':
        time.sleep(1)
        Guardar()
        time.sleep(2)
        Delete()
# Play()
