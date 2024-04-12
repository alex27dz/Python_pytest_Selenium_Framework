
# Import selenium package and setup webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup webdriver + open web
driver = webdriver.Chrome()
driver.get('https://www.google.com/')  # opening the URL/APP
driver.maximize_window()  # maximize window
time.sleep(2)   # naturally sleep for 2s to let the UI page load elements

# locating elements by ID, tag name, xpath, css, text
element = driver.find_element(By.ID, '')
element2 = driver.find_element(By.CLASS_NAME, '')
element3 = driver.find_element(By.XPATH, '')
element4 = driver.find_element(By.NAME, '')
element5 = driver.find_element(By.TAG_NAME, '')
element6 = driver.find_element(By.LINK_TEXT, '')
element7 = driver.find_element(By.PARTIAL_LINK_TEXT, '')
element8 = driver.find_element(By.CSS_SELECTOR, '')

# Getting data, sending data, clicking, screenshotting
element.send_keys()
data = element.text
element.click()

# Waiting - Implicit wait - regular wait
driver.implicitly_wait(10)

# Waiting - Explicit wait - until certain element is located
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "myElementId")))






# edge cases

# pop up windows - handle bmw page

# tabs switch windows


# pop up and tabs windows

# screenshot

# scrolling


# pop up windows, jump on other tabs

# error codes

# Selenium - exemptions handling

# Stail elements exception

# How to test broken links in selenium

# Exceptions

# download files upload files

# closing driver
driver.close()
driver.quit()













