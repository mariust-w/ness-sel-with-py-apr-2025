import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v133.fed_cm import click_dialog_button

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_assign4():
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

    complete_assign4(driver)

    time.sleep(2)
    driver.close()

def complete_assign4(driver):
    driver.find_element(By.CSS_SELECTOR, 'input[id="twotabsearchtextbox"]').send_keys('bluetooth headphones')
    driver.find_element(By.ID, 'nav-search-submit-button').click()
    driver.find_element(By.ID, 'a-autoid-0-announce').click()
    driver.find_element(By.ID, 's-result-sort-select_4').click()

    assert driver.find_element(By.XPATH, '//div[@role="listitem"][1]//div[@data-cy="delivery-recipe"]//span/span[2]').text \
        .__contains__('Apr')

'''
Test Automation – Assignment IV

Application to be tested - URL: 
https://www.amazon.in

Instructions:
•	Use different locators
•	Include Assert statements
•	If any of the steps is missing for the test scenario, you can pick alternate step/scenario from the same website and proceed with the automation
•	Use Chrome Browser
•	Include Time delays ( sleep/implicit/explicit) wherever needed

Tasks:
•	Go to amazon.in
•	Enter “bluetooth headphones” in searchbox and select “electronics” from the categories dropdown
•	Click Search button
•	Select “Newest arrivals”

Validate if the item displayed at the top has current date with “Sep” in it. 
Select get it by today
 
Refer screenshot for each step
'''