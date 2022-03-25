import datetime
from time import sleep
from selenium import webdriver  # import Selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select # <-- add this import for drop down list
from selenium.webdriver import Keys

from selenium.webdriver.chrome.options import Options
s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)

# user_system_id=''
# # create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning
# driver = webdriver.Chrome('../chromedriver.exe')
# # driver = webdriver.Chrome('C:\Automation\Python\pytho_cctb\chromedriver.exe')

# Advantage Shopping Cart Test Automation Plan

# launch Advantage Shopping Cart App Website  - validate we are on the home page
def setUp():
    print("*-------------------------------------------------------*")
    print(" Advantage Shooping Cart App   -----      by Wook Huang  ")
    print(" Lab2. Automation script for setUp() and tearDown() "     )
    print("*-------------------------------------------------------*")
    print("")
    print(f' ### Launch {locators.app} App ### ')
    print(f'*--------------------------------------------------------------------------------------------*')
    print(f' Test Start time : {datetime.datetime.now()}')
    print(f'*--------------------------------------------------------------------------------------------*')
    # Make browser full screen
    driver.maximize_window()
    # Give the browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(locators.adshopcart_url)

    ## Check that Advantage Shopping URL and the home page titles are displayed

    if driver.current_url == locators.adshopcart_url and locators.adshopcart_home_page_title in driver.title:
        print(f'*---Checking Title and URL------------------------------------------------------------------*')
        print(f' {locators.app} websites launched successfully!')
        print(f' Current URL   : {driver.current_url}')
        print(f' Homepage title: {driver.title}')
        print(f'*--------------------------------------------------------------------------------------------*')
        sleep(3) # holding website for 3seconds otherwise close very quickly
    else:
        print(f'*--------------------------------------------------------------------------------------------*')
        print(f'{locators.app} did not launch. Check your code or the application')
        print(f' Current URL   : {driver.current_url}')
        print(f' Homepage title: {driver.title}')
        print(f'*--------------------------------------------------------------------------------------------*')
        tearDown()
    #
def tearDown():
    if driver is not None:
        print(f'*--------------------------------------------------------------------------------------------*')
        print(f'The test is completed at : {datetime.datetime.now()}')
        print(f'*--------------------------------------------------------------------------------------------*')
        sleep(3)
        driver.close()
        driver.quit()

setUp()
tearDown()
