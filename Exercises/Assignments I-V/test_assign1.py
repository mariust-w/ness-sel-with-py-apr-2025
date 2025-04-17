import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_assign1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://ebay.com")

    driver.find_element(By.CSS_SELECTOR, 'input#gh-ac').send_keys("Selenium")
    driver.find_element(By.CSS_SELECTOR, '.gh-search-button__wrap button').click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.fake-tabs__item:last-child').click()
    driver.find_element(By.XPATH, '//span[starts-with(text(),"Sort:")]').click()
    driver.find_element(By.LINK_TEXT, 'Time: newly listed').click()

    assert driver.find_element(By.XPATH,\
    '(//li[contains(@class,"s-item")][1]//span[contains(@class,"s-item__listingDate")])').text\
        .__contains__('Apr')

    time.sleep(2)
    driver.close()

    # Test Automation – Assignment - I
    #
    # Application to be tested - URL: https: // www.ebay.com
    #
    # Instructions:
    # •    Use different locators
    # •    Include Assert statements
    # •    If any of the steps is missing for the test scenario, you can pick alternate step / scenario from the same website and proceed with the automation
    # •    Use Chrome Browser
    # •    Include Time delays(sleep / implicit / explicit) wherever needed
    #
    # Tasks:
    # •    Go to ebay.com
    # •    Enter “Selenium” in searchbox
    # •    Click Search button
    # •    Click  “Buy it now” tab
    # •    Select “Time: newly listed”
    # Validate if the item displayed at the top has current date with “Sep” in it.
    # Refer screenshot for each step