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
from day5.TestUtil import wait_for_element


def test_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(AppData.base_url)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(2) input").send_keys("Admin")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(3) input").send_keys("admin123")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button:only-child").click()

    try:

        element = wait_for_element(driver, By.CSS_SELECTOR, "img+p")
        element.click()

        element = wait_for_element(driver, By.CSS_SELECTOR, "span+ul > li:nth-child(4) > a")
        element.click()

    except Exception:
        time.sleep(3)
        driver.get_screenshot_as_file("error.png")

    time.sleep(3)
    assert 'auth/login' in driver.current_url

    driver.close()


