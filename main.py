from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time 

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = Chrome(PATH)

list_of_cards = []

with open('text_data/cardlist.txt', 'r') as r:
    for link in r:
        list_of_cards.append(str(link))

with open('text_data/prices.txt','w') as f:
    for card in list_of_cards:
        driver.get(card)

        time.sleep(1)

        price = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/section[2]/section/div/div[2]/section[2]/section[1]/div/section[2]/span')
        name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/section[2]/section/div/div[2]/div/h1')

        f.write(f"{name.text}: {price.text} \n")

print("File saved")

driver.quit()