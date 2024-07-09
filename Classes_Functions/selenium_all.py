
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

# closing driver
driver.close()
driver.quit()

# pop up windows | Tabs # tabs switch windows
def tabsopener():
    driver.get('https://www.bmw.ca/')  # Open the first tab with a specific URL
    driver.execute_script("window.open('');")  # Open a second tab using JavaScript
    driver.switch_to.window(driver.window_handles[1])  # Now, the browser has two tabs, switch to the new tab using window_handles
    driver.get('https://www.bing.com')  # Navigate to a different URL in the second tab
    time.sleep(2)
    # Switch back to the first tab if needed
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # Switch back to the second tab if needed
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)


# Shadow-root - Javascript execution
# executing Javascript to work with the shadow-root elements
def bmw_homepage_popup_shadow_root():
    driver.get('https://www.bmw.ca/')  # opening the URL/APP
    driver.maximize_window()  # maximize window
    time.sleep(3)  # Better to use WebDriverWait instead of sleep where possible.

    # Replace 'host-element-selector' with the selector + 'button-selector-inside-shadow' with the selector inside the DOM
    element = driver.execute_script("""
        var host = document.querySelector('epaas-consent-drawer-shell');
        var shadowRoot = host.shadowRoot;
        return shadowRoot.querySelector('button.accept-button');
    """)

    # Click the element
    driver.execute_script("arguments[0].click();", element)
    print('shadow-root pop up ')
    time.sleep(3)
    # Always a good practice to close the browser when done
    driver.quit()

# download files upload files
# edge cases
# screenshot
# scrolling
# error codes - Exceptions handling Stale elements exception
# How to test broken links in selenium







