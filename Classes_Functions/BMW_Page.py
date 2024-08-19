# Import selenium package and setup webdriver
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller


# Automatically install and set up ChromeDriver
# chromedriver_autoinstaller.install()
# ChromeDriverManager().install()
# setup webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

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

bmw_homepage_popup_shadow_root()


