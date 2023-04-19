from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service('<CHROMEDRIVER_PATH>'))
driver.get("https://www.google.com/search?q=weather&oq")

print("Current weather for Local Area:")
celsius = driver.find_element(By.ID, 'wob_tm').text
area = driver.find_element(By.CLASS_NAME, 'BBwThe').text
wind = driver.find_element(By.ID, 'wob_ws').text
humidity = driver.find_element(By.ID, 'wob_hm').text
currentTime = driver.find_element(By.ID, 'wob_dts').text
tomorrow = driver.find_element(By.XPATH, '//div/div/div[3]/div[3]/div/div[2]/div[1]').text
minWeather = driver.find_element(By.XPATH, '//div[3]/div[3]/div/div[2]/div[3]/div[2]/span/span[1]').text
maxWeather = driver.find_element(By.XPATH, '//div[3]/div[3]/div/div[2]/div[3]/div[1]/span/span[1]').text
print('Current celsius:', celsius, '°C in', area)
print('Celsius (Min-Max):', minWeather, '°C Up to', maxWeather, '°C')
print(humidity, 'humidity')
print('Wind speed:', wind)
print('Current time and day:', currentTime)
print()
driver.find_element(By.ID, 'dimg_3').click()
celsius = driver.find_element(By.ID, 'wob_tm').text
area = driver.find_element(By.CLASS_NAME, 'BBwThe').text
wind = driver.find_element(By.ID, 'wob_ws').text
humidity = driver.find_element(By.ID, 'wob_hm').text
currentTime = driver.find_element(By.ID, 'wob_dts').text
minWeather = driver.find_element(By.XPATH, '//div[3]/div[3]/div/div[1]/div[3]/div[2]/span/span[1]').text
maxWeather = driver.find_element(By.XPATH, '//div[3]/div[3]/div/div[1]/div[3]/div[1]/span/span[1]').text
print('Weather for tomorrow:', '(', tomorrow, ')')
print('Celsius (Min-Max):', minWeather, '°C Up to', maxWeather, '°C')
print(humidity, 'humidity')
print('Wind speed:', wind)
