import os
import random
import string
import time
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from server.db import connection


def get_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=chrome_options)

    try:
        driver.maximize_window()
        driver.get(url)

        if not os.path.exists("client/src/assets/images"):
            os.makedirs("client/src/assets/images")

        timestamp = int(time.time() * 1000)
        random_num = random.randint(1, 100)
        filename = f"{timestamp}-{random_num}.png"
        screenshot_path = os.path.join("client/src/assets/images", filename).replace('\\', "/")

        driver.save_screenshot(screenshot_path)

        return filename
    finally:
        driver.quit()

def generate_short_url(original_url):
    alphabet = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(alphabet) for _ in range(6))
        parsed_url = urlparse(original_url)
        domain = parsed_url.scheme + '://' + parsed_url.netloc + '/'
        short_url = domain + short_code
        with connection.cursor() as cursor:
            cursor.execute('SELECT id FROM shorturls WHERE shorturl = %s', (short_url,))
            record = cursor.fetchone()
            if not record:
                return short_url


def save_url(original_url):
    short_url = generate_short_url(original_url)
    screenshot_data = get_screenshot(original_url)
    try:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO shorturls (firsturl, shorturl) VALUES (%s, %s)',(original_url, short_url))
            connection.commit()
    except ExceptionGroup as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        return short_url, screenshot_data