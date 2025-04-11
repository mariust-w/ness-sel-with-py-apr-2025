import time
import os

from selenium import webdriver
import pytest

# test method
def test_googletest():

    os.chdir("../lib")
    # print(os.getcwd())

    # launch the browser
    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    # navigate to the app url
    driver.get("https://google.com")

    # time delay
    time.sleep(5)

    # maximize the window
    driver.maximize_window()

    # to close the window
    driver.close()


    '''
    
    Script --> Client library --> ChromeDriver --> Browser
     
    
    '''