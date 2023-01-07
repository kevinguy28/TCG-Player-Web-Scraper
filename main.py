from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time 

options = Options()
options.headless = True
userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"
options.add_argument(f'user-agent={userAgent}')

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = Chrome(PATH, chrome_options=options)

list_of_cards = []

with open('text_data/cardlist.txt', 'r') as r:
    for link in r:
        list_of_cards.append(str(link))

with open('text_data/prices.txt','w') as f:
    for card in list_of_cards:
        driver.get(card)

        time.sleep(1)

        price = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section[2]/section/div/div[2]/section[3]/div/section[1]/ul/li[1]/span[2]')
        #//*[@id="app"]/div/div/section[2]/section/div/div[2]/section[2]/section[1]/div/section[2]/span
        name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/section[2]/section/div/div[2]/div/h1')

        f.write(f"{name.text}: {price.text} \n")

print("File saved")

driver.quit()