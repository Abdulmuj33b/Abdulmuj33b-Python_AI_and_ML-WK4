from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://example.com/login")

# Valid credentials
driver.find_element_by_id("username").send_keys("valid_user")
driver.find_element_by_id("password").send_keys("valid_pass")
driver.find_element_by_id("login").click()
assert "Dashboard" in driver.page_source

# Invalid credentials
driver.get("http://example.com/login")
driver.find_element_by_id("username").send_keys("invalid_user")
driver.find_element_by_id("password").send_keys("invalid_pass")
driver.find_element_by_id("login").click()
assert "Invalid credentials" in driver.page_source

driver.quit()

#AI-powered testing tools enhance test coverage by automatically generating test cases, identifying edge cases, and adapting to UI changes. Unlike manual testing, which is time-consuming and prone to human error, AI tools can quickly detect regressions and suggest new tests, improving reliability and reducing maintenance.
