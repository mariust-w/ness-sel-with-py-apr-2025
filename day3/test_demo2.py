import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import pytest

# test method
def test_googletest():

    # launch the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # ser = Service(
    #     executable_path= "chromedriver.exe",
    #     port=9001
    # )


    # opt = Options()
    # opt.add_argument("--start-maximized")


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # navigate to the app url
    driver.get("https://google.com")

    # time delay
    time.sleep(5)

    # maximize the window
    # driver.maximize_window()

    # to close the window
    driver.close()


    '''
    
    id
    name
    classname
    linktext
    partial linktext
    xpath   
        - absolute xpath
             - /html/body
        - relative xpath
             - //div/div..../input
        - xpath axes 
    css selector
    tagname
    relative locators
     
    type - send_keys()
    click - click()
    clear - clear()
    form data submission - submit()
    
    
    '''


