from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from time import sleep
##import tkinter as tk
##from tkinter import ttk 
"""
ventana_principal = tk.Tk()
ventana_principal.config(width=1000, height=500)
ventana_principal.title("BOT")
"""
driver = webdriver.Chrome()
while True:

    
    def login (driver):
    
        driver.get('https://www.instagram.com/accounts/login/')
        sleep(1)
        login_button = driver.find_element(By.NAME, "username")
        login_button.clear()
        login_button.send_keys("eloitraver2@gmail.com")
        login_button.clear()
        sleep(0.3)
        login_button = driver.find_element(By.NAME, "password")
        login_button.clear()
        login_button.send_keys("123456789Hola")
        login_button.clear()
        sleep(0.3)
        login_button.send_keys(Keys.RETURN)
        login_button.clear()
        sleep(20)
"""   
boto_LOGIN = ttk.Button(
    ventana_principal,
    text="Calcular",
    command=login
    )
boto_LOGIN.place(x=400, y=100)
"""



