import pyautogui
import time

def Escritorio1():
    pyautogui.hotkey('ctrl','num1')

def Sheet():
    pyautogui.hotkey('ctrl','1')

def Down():
    pyautogui.press('down')

def  Copy():
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)

def GuiasAnicam():
    pyautogui.hotkey('ctrl','2')
    
def ComandoBuscar():
    pyautogui.hotkey('ctrl','f')

def Paste():
    pyautogui.hotkey('ctrl','v')


    """""#######################################################################"""""

def ComandoCaptureCompleto():
    pyautogui.hotkey('ctrl', 'shift', 'print')
    time.sleep(1)
    pyautogui.mouseDown(x=730, y=385)
    pyautogui.mouseUp(x=1470, y=630)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'num6')
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(x=1723, y=801)
    pyautogui.press('f8')
    pyautogui.click(x=1050, y=674)
    pyautogui.write('Order amazon: ' ,interval=0.15)
    pyautogui.hotkey('ctrl', 'num1' )
    time.sleep(1)
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl','left')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('ctrl','num6')
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    Escritorio1()
    GuiasAnicam()
       
    pyautogui.alert(text='Prsione "OK" luego de pegar el encabezado', title='Pegar encabezado', button='OK')
    pyautogui.hotkey('ctrl','num6')
    
    time.sleep(1)
    pyautogui.hotkey('ctrl','shift', 's')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    MensajeGuerdado = pyautogui.alert(text='Guardado', title='Exitoso!!!', button='OK')
    if MensajeGuerdado == 'OK':
        pyautogui.click()
        pyautogui.hotkey('ctrl','a')        
        pyautogui.press('delete')
        pyautogui.hotkey('ctrl','num4')
        pyautogui.click(x=2939, y=85)


"""###################################################################################"""


"""Aqui va el dividido"""

    




"""#################################################################################"""


Escritorio1()
Sheet()
Down()
Copy()

GuiasAnicam()

ComandoBuscar()
Paste()

time.sleep(2)
mensaje1 = pyautogui.confirm(text='Capturar', title='Seleccione el tipo de captura', buttons=['Completo', 'Dividido'])
time.sleep(1)

if mensaje1 == 'Completo':
    ComandoCaptureCompleto()




