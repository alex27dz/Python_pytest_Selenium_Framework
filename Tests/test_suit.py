from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Timers
delay = 1
short_delay = 0.005
medium_delay = 3
long_delay = 12
start_time = time.perf_counter()
def runtime():
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time)

# Webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())  # Automatically download and set up ChromeDriver

# random test using selenium > opening web > searching > verifying results
def test_something():
    driver.get('https://www.cnn.com/')
    driver.maximize_window()
    time.sleep(3)
    search = driver.find_element(By.XPATH, '//*[@id="headerSearchIcon"]')
    search.click()
    searchbar = driver.find_element(By.XPATH, '//*[@id="pageHeader"]/div/div/div[2]/div/div[1]/form/input')
    searchbar.click()
    searchbar.send_keys('Prigozhin')
    searchbar.send_keys(Keys.RETURN)
    time.sleep(3)
    results_num = driver.find_element(By.XPATH, '//*[@id="search"]/div[2]/div/div[1]/div[1]').text
    print('Results\n', results_num[31:-14])
    driver.close()
    runtime()
    assert results_num[31:-14] == '900', 'not valid, Expected 900 results'



