from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.options import Options


print("Welcome to songs search..")


def searchSong():
    songName = input("Type a song name (Add a bend name to be more specific (Recommended)\nInput: ")
    print("Loading song detail's...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service('C://Users/shayo/chromedriver_win32/chromedriver.exe'), options=chrome_options)
    driver.get("https://www.google.com/search?q=" + songName)
    print('---- General Info ----')
    # driver.find_element(By.XPATH, '/html/body/div[7]/div/div[7]/div[1]/div/div/div[2]/div/a[2]').click()  # change website to EN
    Artist = driver.find_element(By.XPATH, '//div[11]/div[4]/div[3]/div/div/div[2]/div/div/div/div[3]/div/div/div').text
    print(Artist)
    Album = driver.find_element(By.XPATH, '//div[11]/div[4]/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div').text
    print(Album)
    distributionDate = driver.find_element(By.XPATH, '//div[11]/div[4]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div').text
    print(distributionDate)
    print('---- Lyrics ----')
    driver.find_element(By.XPATH, '//div/div/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/a').click()
    driver.implicitly_wait(7)
    myButton = driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div/div/div[1]/div/div')
    Lyrics = driver.find_element(locate_with(By.XPATH, "//div[3]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div[2]").below(myButton)).text
    print(Lyrics)
    print('---- Song Info ----')


searchSong()

while True:
    keep = input("Would you want to search more songs? (Y/N): ")
    try:
        if keep == 'y':
            searchSong()
        elif keep == 'n':
            print("Test ended.")
            break
    except ValueError:
        print("Invalid input.")
    continue


