from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()

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
    

login (driver)


