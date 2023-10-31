import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Use ChromeDriverManager to download and set up the ChromeDriver executable
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.google.com')
time.sleep(10)


