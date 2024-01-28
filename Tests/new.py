
def seleniumopenweb():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    driver.maximize_window()
    time.sleep(2)

char = 'alex'
age = 15
myname = True

print(type(myname))

seleniumopenweb()


