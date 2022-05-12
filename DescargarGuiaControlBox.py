import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://aduanas.colocarcourier.com/Children/Details?childNo="
Listaguia = [
 'BOG3064700040']

for item in Listaguia:
    print(item)

    url = link + item

    driver = webdriver.Chrome()
    driver.get(url)



    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[3]/a[1]")))

    finally:
        print("Elemento encontrado")


    ClickDescargar =  driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[3]/a[1]")
    ClickDescargar.click()
    time.sleep(6)
    print("Descargada")
    driver.close()
