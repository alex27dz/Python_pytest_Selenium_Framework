# Import selenium package and setup webdriver
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
original_window = driver.current_window_handle  # original window handle for later use
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait for new window/tab

# Iterate through available window handles and switch to the new one
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Now you can interact with the new window
print("New window title: " + driver.title)


# Alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Simple Alert says: ", alert.text)
alert.accept()

confirm_button = driver.find_element(By.ID, 'confirm-alert')
confirm_button.click()

# Wait for the alert and dismiss it (click 'Cancel')
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Confirmation Alert says: ", alert.text)
alert.dismiss()
# Use alert.accept() to click 'OK'

# Example to trigger and handle a prompt
prompt_button = driver.find_element(By.ID, 'prompt-alert')
prompt_button.click()

# Wait for the prompt, send some text, and accept it
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("Hello, this is a test.")
print("Prompt Alert says: ", alert.text)
alert.accept()

# Clean up
driver.quit()

# When done, close the new window and switch back to the original window
driver.close()
driver.switch_to.window(original_window)

# Continue with other tasks in the original window
'''

# setup webdriver + open web
driver = webdriver.Chrome()

driver.get("https://www.example.com")  # Replace with the actual URL

# Execute JavaScript to find the element within the shadow root
element = driver.execute_script("""
var shadowHost = document.querySelector('#shadow-host');  // Replace with your actual shadow host selector
var shadowRoot = shadowHost.shadowRoot;
var deepNestedElement = shadowRoot.querySelector('div > div > button[data-testid="uc-accept-all-button"]');
return deepNestedElement;
""")

# Interact with the element if not None
if element:
    driver.execute_script("arguments[0].click();", element)



def bmwhomepagepopup():
    driver.get('https://www.bmw.ca/')  # opening the URL/APP
    driver.maximize_window()  # maximize window
    time.sleep(3)  # Better to use WebDriverWait instead of sleep where possible.

    # Execute JavaScript to access the shadow root and then the element inside it
    desired_element = driver.execute_script("""
        var host = arguments[0];
        var shadowRoot = host.shadowRoot;
        return shadowRoot.querySelector('button[data-testid=\"uc-accept-all-button\"]');  # Updated selector for clarity and correctness.
    """)

    driver.execute_script("arguments[0].click();", desired_element)  # Click on the element
    time.sleep(5)  # Again, prefer WebDriverWait to manage timing.
    driver.quit()







