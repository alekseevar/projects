from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
import pandas as pd

options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')

website = "https://rieltor.ua/kiev/flats-rent/#10.5/50.4333/30.5167"
path = "/Users/ruslanaalekseeva/ruslana/chromedriver_mac_arm64_2/chromedriver"
service = ChromeService(path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
time.sleep(5)

last_page = driver.find_elements(By.CLASS_NAME, "pager-btn")[-1].text
print(last_page)
flats = []
for page_number in range(1, 4):
    """https://rieltor.ua/kiev/flats-rent/?page=3"""
    driver.get(f"https://rieltor.ua/kiev/flats-rent/?page={page_number}")

    containers_flat = driver.find_elements(By.XPATH, '//div[contains(@data-jss, "catalog")]')
    time.sleep(5)
    for container in containers_flat:
        flat = []
        price = container.find_element(By.XPATH, './/strong[contains(@class, "price")]').text
        #print(price)
        flat.append(price)
        address = container.find_element(By.XPATH, './/div[contains(@class, "address")]').text
        #print(address)
        flat.append(address)
        regions = container.find_elements(By.XPATH, './/a[contains(@data-analytics-event, "region")]')
        #print(" ".join([each.text for each in regions]))
        flat.append(" ".join([each.text for each in regions]))
        rooms = container.find_element(By.XPATH, './/span[contains(text(), "кімнат")]').text
        flat.append(rooms)
        area = container.find_element(By.XPATH, './/span[contains(text(), "м²")]').text
        flat.append(area)
        floor = container.find_element(By.XPATH, './/span[contains(text(), "поверх")]').text
        flat.append(floor)
        flats.append(flat)

df_flats = pd.DataFrame(flats, columns=["price", "address", "region", "rooms", "area", "floor"])
df_flats.to_csv("flats_from_rieltor_ua.csv", index=False)
print(df_flats)




