import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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

def test_key_actions(setup):

    username_field = driver.find_element(By.NAME,'username')
    ActionChains(driver)\
        .move_to_element(username_field)\
        .pause(3)\
        .click_and_hold()\
        .pause(3)\
        .send_keys('abd')\
        .pause(2)\
        .key_down(Keys.SHIFT)\
        .send_keys('Admin')\
        .key_up(Keys.SHIFT)\
        .pause(3)\
        .double_click()\
        .send_keys(Keys.BACKSPACE)\
        .pause(3)\
        .perform()

    time.sleep(5)