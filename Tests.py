from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service("/chromedriver.exe"))

driver.get("https://www.google.com")
title = driver.title
print(title)
driver.refresh()
if title == driver.title:
    print("the title are equal")
else:
    print("the title aren't equal")
driver.get("https://translate.google.com/")
driver.find_element(By.CLASS_NAME, value="er8xn").send_keys("Hello")
driver.get("https://www.youtube.com/")
driver.find_element(By.CLASS_NAME, value="style-scope ytd-searchbox").send_keys("Rick Astley - Never Gonna Give You Up")
driver.find_element(By.ID, value="search-icon-legacy").click()
driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR, value="input[id=email]").clear()
driver.find_element(By.CSS_SELECTOR, value="input[id=pass]").clear()
driver.find_element(By.CSS_SELECTOR, value="input[id=email]").send_keys("Email")
driver.find_element(By.CSS_SELECTOR, value="input[id=pass]").send_keys("Password")
driver.get("https://github.com/")
driver.find_element(By.XPATH, value="/html//form/label/input[1]").send_keys("Selenium")
driver.find_element(By.XPATH, value="/html//form/label/input[1]").send_keys(Keys.ENTER)
