import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://ebay.com')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.find_element(By.NAME,'_nkw').send_keys("The Fountain head")

    catydropdown = driver.find_element(By.CSS_SELECTOR,'.gh-search-categories')
    categories = Select(catydropdown)

    # categories.select_by_visible_text("Books")
    categories.select_by_value("267")

    time.sleep(3)
    va_books = driver.find_element(By.CSS_SELECTOR,'option:nth-child(5)').get_attribute('value')
    print(va_books)

    driver.find_element(By.XPATH,"//span[text()='Search']").click()

    driver.close()



