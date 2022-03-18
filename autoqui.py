import pyautogui
import time


def Escritorio1():
    pyautogui.hotkey('ctrl','num1')

def Sheet():
    pyautogui.hotkey('ctrl','1')

def Down():
    pyautogui.press('down')

def Copy():
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)

def GuiasAnicam():
    pyautogui.hotkey('ctrl','2')
    
def ComandoBuscar():
    pyautogui.hotkey('ctrl','f')

def Paste():
    pyautogui.hotkey('ctrl','v')

time.sleep(1)

Escritorio1()
Sheet()
Down()
Copy()

GuiasAnicam()

ComandoBuscar()
time.sleep(1)
Paste()

time.sleep(2)
mensaje1 = pyautogui.confirm(text='Si la encontro presione OK', title='¿Encontrado?', buttons=['OK', 'Cancelar'])
print(mensaje1)

if mensaje1=='Cancelar':
    print("No encontrado")
else:
    time.sleep(1)
    Down()
    pyautogui.hotkey('ctrl', 'shift', 'print')
    time.sleep(1)
    pyautogui.mouseDown(x=706, y=516)
    pyautogui.mouseUp(x=1490, y=1035)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'num6')
    pyautogui.click()
    Paste()
    time.sleep(1)
    pyautogui.click(x=1726, y=763)
    pyautogui.press('f8')
    pyautogui.click(x=1109, y=753)
    pyautogui.write('Order: ', interval=0.15)
    pyautogui.hotkey('ctrl', 'num1' )
    time.sleep(2)
    pyautogui.hotkey('ctrl', '1' )
    time.sleep(1)
    pyautogui.hotkey('ctrl','left')
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('ctrl','right')
    time.sleep(1)
    pyautogui.hotkey('ctrl','num6')
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    Guardar = pyautogui.alert(text='Guardar', title='Si esta todo bien, presione OK', button='OK')
    time.sleep(1)
    pyautogui.press('f1')
    
    pyautogui.hotkey('ctrl','shift', 's')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    Guardado = pyautogui.alert(text='Guardado', title='Exitoso!!!', button='OK')
    print(Guardado)
    time.sleep(2)

    pyautogui.press('f1')

    pyautogui.hotkey('ctrl','a')

    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.hotkey('ctrl','num4')

    pyautogui.click(x=3751, y=79)
        