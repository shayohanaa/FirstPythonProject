from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
import time


contact = "you" # the contact you want to send a message
content = "This text sent via selenium." # the text you want to send

driver = webdriver.Chrome(service=Service("<PATH_TO_CHROMEDRIVER"))
driver.get("https://web.whatsapp.com/")
print("Scan QR Code, and then press 'ENTER'")
input()
print("Logged in.")
action = ActionChains(driver)

search = driver.find_element(By.XPATH, value="//div[1]/div/div/div[2]/div/div[1]/p")
action.click(search)
action.perform()

action.send_keys(contact)
action.perform()

chosen_contact = driver.find_element(locate_with(By.XPATH, "//div[1]/div/div/div[2]"))
choose = driver.find_element(locate_with(By.CLASS_NAME, "rx9719la").below(chosen_contact))
action.click(choose)
action.perform()

xpath_input = driver.find_element(By.XPATH, value="//footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
action.click(xpath_input)
action.perform()

action.send_keys(content)
action.perform()

action.send_keys(Keys.ENTER)
action.perform()
