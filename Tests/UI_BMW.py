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
driver.maximize_window()
time.sleep(2)











