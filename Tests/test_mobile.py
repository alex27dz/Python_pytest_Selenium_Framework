#  Example 1: Searching in a Mobile Browser

import pytest
from appium import webdriver
import time


@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "your_device_name",
        "browserName": "Chrome"  # Use Chrome browser
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    yield driver

    driver.quit()


def test_mobile_browser_search(driver):
    driver.get("https://www.google.com")

    search_box = driver.find_element_by_name("q")
    search_box.send_keys("Appium tutorial")
    search_box.submit()

    time.sleep(2)

    # Verify search results page title
    assert "Appium tutorial" in driver.title


if __name__ == "__main__":
    pytest.main()




#  Example 2: Interacting with Mobile List

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "your_device_name",
        "appPackage": "com.example.app",  # Replace with actual app package name
        "appActivity": "com.example.app.MainActivity"  # Replace with actual app activity name
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    yield driver

    driver.quit()


def test_mobile_list_interaction(driver):
    # Scroll down in the list
    driver.swipe(start_x=500, start_y=1400, end_x=500, end_y=200, duration=800)
    time.sleep(1)

    # Click on the second item in the list
    item = driver.find_elements_by_id("com.example.app:id/list_item")[1]
    item.click()

    # Perform assertions or interactions with the selected item's details
    # ...


if __name__ == "__main__":
    pytest.main()



#  Example 3: Logging In to a Mobile App

import pytest
from appium import webdriver
import time


@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "your_device_name",
        "appPackage": "com.example.app",
        "appActivity": "com.example.app.MainActivity"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    yield driver

    driver.quit()


def test_mobile_app_login(driver):
    # Navigate to the login screen
    login_button = driver.find_element_by_id("com.example.app:id/login_button")
    login_button.click()

    # Enter username and password
    username_field = driver.find_element_by_id("com.example.app:id/username_field")
    password_field = driver.find_element_by_id("com.example.app:id/password_field")

    username_field.send_keys("your_username")
    password_field.send_keys("your_password")

    # Click the login button
    submit_button = driver.find_element_by_id("com.example.app:id/submit_button")
    submit_button.click()

    # Wait for the dashboard screen to load
    time.sleep(2)

    # Verify successful login
    assert "Dashboard" in driver.page_source


if __name__ == "__main__":
    pytest.main()
