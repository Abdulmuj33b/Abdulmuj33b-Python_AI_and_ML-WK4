from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver (ensure chromedriver is in your PATH or specify the path)
driver = webdriver.Chrome()

try:
    # Test valid credentials
    driver.get("http://example.com/login")  # TODO: Replace with your login page URL
    driver.find_element(By.ID, "username").send_keys("valid_user")  # TODO: Replace with valid username
    driver.find_element(By.ID, "password").send_keys("valid_pass")  # TODO: Replace with valid password
    driver.find_element(By.ID, "login").click()
    time.sleep(2)  # Wait for page to load
    if "Dashboard" in driver.page_source:
        print("Valid login: SUCCESS")
    else:
        print("Valid login: FAILURE")

    # Test invalid credentials
    driver.get("http://example.com/login")  # TODO: Replace with your login page URL
    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("invalid_pass")
    driver.find_element(By.ID, "login").click()
    time.sleep(2)
    if "Invalid credentials" in driver.page_source:
        print("Invalid login: SUCCESS (error shown)")
    else:
        print("Invalid login: FAILURE (no error shown)")

finally:
    driver.quit() 