from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

opt = Options()
opt.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Remove extra quotes
opt.add_argument("--incognito")
"""
driver = webdriver.Chrome(
    ChromeDriverManager().install(),
    options=opt 
    )
    """ # --> options=opt dona error 
#driver.get("https://www.instagram.com")
sleep(3)
