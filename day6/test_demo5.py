import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

import pytest

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture()
def setup():
    global driver
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_switch_window(setup):
    driver.find_element(By.PARTIAL_LINK_TEXT,'Orange').click()
    time.sleep(3)

    parent_window = driver.current_window_handle
    print('Parent window :', parent_window)

    handles = driver.window_handles
    for handle in handles:
        print(handle)

    time.sleep(2)
    print('Child window : ',driver.window_handles[1] )
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'div.web-menu-btn ul > li:last-child button').click()

    time.sleep(5)

