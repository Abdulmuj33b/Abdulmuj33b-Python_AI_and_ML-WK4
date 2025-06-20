from selenium import webdriver

# If chromedriver.exe is not in your PATH, specify the path:
# driver = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://www.google.com")
print(driver.title)
driver.quit()