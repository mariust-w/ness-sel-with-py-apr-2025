import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://ebay.com')
    time.sleep(5)

    categorylist = driver.find_elements(By.TAG_NAME,'option')
    for category in categorylist:
        print(category.text)


    driver.close()



