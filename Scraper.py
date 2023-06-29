from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

apartments_list = []

for x in range(1,101):
    url = 'https://www.4zida.rs/prodaja-stanova/beograd?strana='
    driver.get(url + str(x))

    wait = WebDriverWait(driver, 10)

    try:
        apartments = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ed-card-details')))
    except NoSuchElementException:
        continue

    for apartment in apartments:
        try:
            price_in_eur = apartment.find_element(By.XPATH, './/*[@id="internal"]/div[1]/span').text.split(" ")[0].replace(".", "")
            price_per_sq_meter = apartment.find_element(By.XPATH, './/*[@id="internal"]/p').text.split(" ")[0].replace(".", "")
            size_sq_meter = apartment.find_element(By.XPATH, './/*[@id="internal"]/span/strong[1]').text.split("m")[0]
            number_of_rooms = apartment.find_element(By.XPATH, './/*[@id="internal"]/span/strong[2]').text.split(".")[0].split(" ")[0]
            location = apartment.find_element(By.XPATH, './/*[@id="internal"]/div[2]/span[1]').text
            area = apartment.find_element(By.XPATH, './/*[@id="internal"]/div[2]/span[2]').text.split(',')[0]
            apartments_items = {
                "price_in_eur": price_in_eur,
                "price_per_sq_meter": price_per_sq_meter,
                "size_sq_meter": size_sq_meter,
                "number_of_rooms": number_of_rooms,
                "location": location,
                "area": area
            }
            apartments_list.append(apartments_items)
        except NoSuchElementException:
            continue

df = pd.DataFrame(apartments_list)
df.to_csv('data.csv', index=False)
