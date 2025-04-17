import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v133.fed_cm import click_dialog_button

from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_assign3():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.myntra.com")

    driver.find_element(By.CSS_SELECTOR, ".desktop-searchBar").send_keys('Bluetooth headphones')
    # from the next line it fails on my machine; it's like the site does not exist
    '''
    This site can’t be reached
    The webpage at https://www.myntra.com/bluetooth-headphones might be temporarily down or it may have moved permanently to a new web address.
    ERR_HTTP2_PROTOCOL_ERROR
    '''
    driver.find_element(By.XPATH, '//a[@class="desktop-submit"]').click()
    driver.find_element(By.CSS_SELECTOR, '.vertical-filters-label input[value="JBL"]').click()

    assert driver.find_element(By.XPATH, '//ul/li[1]//h3').text\
        .__contains__('JBL')

    time.sleep(2)
    driver.close()

'''
Test Automation – Assignment III

Application to be tested - URL: 
https://www.myntra.com 

Instructions:
•	Use different locators
•	Include Assert statements
•	If any of the steps is missing for the test scenario, you can pick alternate step/scenario from the same website and proceed with the automation
•	Use Chrome Browser
•	Include Time delays ( sleep/implicit/explicit) wherever needed

Tasks:
•	Go to myntra.com
•	Enter “Bluetooth headphones” in searchbox  
•	Click Search button
•	Select “whats new”
Select brand as JBL
Validate if the item displayed at the top has brand name as JBL in it. 
Refer screenshot for each step
'''