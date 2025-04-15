import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

import pytest

from day5.AppData import AppData

driver =""

@pytest.fixture()
def init():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(AppData.base_url)
    driver.maximize_window()
    time.sleep(3)
    yield
    driver.close()


def test_login(init):

    driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(2) input").send_keys("Admin")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(3) input").send_keys("admin123")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button:only-child").click()

    try:
        # wait = WebDriverWait(driver,10)
        wait = WebDriverWait(driver, 10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img+p")))

        # driver.find_element(By.CSS_SELECTOR, "img+p").click()
        element.click()

        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span+ul > li:nth-child(4) > a")))
        # driver.find_element(By.CSS_SELECTOR, "span+ul > li:nth-child(4) > a").click()
        element.click()
    except Exception:
        driver.get_screenshot_as_file("error.png")

    time.sleep(3)
    assert 'auth/login' in driver.current_url


# <li>
#     <span>
#     <ul>
#     <p>
#
# </li>
#
# span+ul
# span~p
# li > ul
# ul:nth-child(2)
# ul:nth-of-type(1)
