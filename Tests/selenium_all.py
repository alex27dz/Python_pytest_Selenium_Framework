
# Import selenium package setup webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# opening the URL/APP
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(2)


# locating elements by ID, tag name, xpath, css, text

# Getting data, sending data, clicking, screenshotting

# Waiting for elements, time

# pop up windows, jump on other tabs

# error codes

# Selenium - exemptions handling

# Stail elements exception

# How to test broken links in selenium

# Exceptions

# closing driver
driver.close()
driver.quit()













