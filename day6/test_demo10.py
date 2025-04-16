import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import pytest


def test_mouse_actions():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)

    element_list = driver.find_elements(By.XPATH,"//div/preceding::input")
    for element in element_list:
        print(element.tag_name)
    time.sleep(5)
    driver.quit()
