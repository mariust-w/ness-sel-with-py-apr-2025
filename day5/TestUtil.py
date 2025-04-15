from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def wait_for_element(driver,by,value,timeout=10,poll_frequency=2):

    wait = WebDriverWait(driver,timeout=timeout,poll_frequency=poll_frequency,ignored_exceptions=[NoSuchElementException])
    wait.until(EC.visibility_of_element_located(by,value))
    return driver.find_element(by,value)


