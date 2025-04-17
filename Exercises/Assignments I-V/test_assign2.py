import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v133.fed_cm import click_dialog_button

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_assign2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.amazon.in")

    try:
        # this is to bypass robot check
        if driver.find_element(By.CSS_SELECTOR, 'a[onclick="window.location.reload()"]').is_displayed():
            driver.find_element(By.CSS_SELECTOR, 'a[onclick="window.location.reload()"]').click()
    except NoSuchElementException:
        print("No robot check to bypass")

    complete_assign2(driver)

    time.sleep(2)
    driver.close()

def complete_assign2(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href^='/deals']").click()
    driver.find_element(By.XPATH, '//a[@aria-label="Clearance"]').click()
    # next line might fail, as the "Watches" item is not always present on page
    driver.find_element(By.XPATH, '//ul[@aria-labelledby="n-title"]//span[text()="Watches"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[aria-label*="Get It Today"]').click()

    assert driver.find_element(By.CSS_SELECTOR, 'span[data-component-id="3"] h2').text == 'Results'
    # next line might fail, as the "Watch" word is not always part of the item name
    assert driver.find_element(By.CSS_SELECTOR, 'div[data-index="2"] div[data-cy="title-recipe"] a').text \
        .__contains__('Watch')

'''
Test Automation - Assessment II

Application to be tested - URL: 
https://www.amazon.in

Instructions:
•	Use different locators
•	Include Assert statements
•	If any of the steps is missing for the test scenario, you can pick alternate step/scenario from the same website and proceed with the automation
•	Use Chrome Browser
•	Include Time delays ( sleep/implicit/explicit) wherever needed

Tasks:
•	Go to https://www.amazon.in
•	Click the “Today’s Deals” tab
•	Click the “Clearance” link
•	Click “Watches”
•	Click “Get it Today” checkbox
•	Validate if “RESULTS” message is displayed
•	Validate if the first item has item name containing “Watch”
Refer screenshot for each step
'''