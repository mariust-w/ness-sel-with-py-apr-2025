import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)

    username_field = driver.find_element(locate_with(By.NAME,"username").above({By.NAME:"password"}))
    username_field.send_keys("Admin")
    time.sleep(3)

    password_field = driver.find_element(locate_with(By.NAME, "password").below({By.NAME: "username"}))
    password_field.send_keys("admin123")

    time.sleep(3)
    driver.find_element(By.TAG_NAME,"button").click()

    time.sleep(3)
    driver.close()



