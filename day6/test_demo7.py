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
    driver.get('https://jqueryui.com/droppable/')
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_mouse_actions(setup):

    driver.switch_to.frame(0)

    draggable = driver.find_element(By.CSS_SELECTOR,"div#draggable")
    droppable = driver.find_element(By.CSS_SELECTOR,"div#droppable")
    # ActionChains(driver).drag_and_drop(draggable,droppable).perform()

    ActionChains(driver) \
        .move_to_element(draggable) \
        .pause(3) \
        .click_and_hold() \
        .pause(3) \
        .move_to_element(droppable) \
        .pause(3) \
        .release() \
        .pause(3) \
        .click_and_hold() \
        .move_by_offset(30,60)\
        .release() \
        .perform()

    time.sleep(5)