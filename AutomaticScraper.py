from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler

def scrape_data():
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
    df['price_in_eur'] = pd.to_numeric(df['price_in_eur'])
    df['price_per_sq_meter'] = pd.to_numeric(df['price_per_sq_meter'])
    df['size_sq_meter'] = pd.to_numeric(df['size_sq_meter'])
    df.to_excel('data.xlsx', index=False)
    driver.quit()

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the scraper to run every day at a specific time (change as needed)
scheduler.add_job(scrape_data, 'cron', day_of_week='*', hour='11', minute='32')

# Start the scheduler
scheduler.start()
