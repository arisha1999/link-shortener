import os
import random
import string
import time
from urllib.parse import urlparse

import psycopg2
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
CORS(app)

host = "127.0.0.1"
user = "postgres"
password = "qwerty"
db_name = "test_urls"

def get_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

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
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    while True:
        short_code = ''.join(random.choice(alphabet) for _ in range(6))
        parsed_url = urlparse(original_url)
        domain = parsed_url.scheme + '://' + parsed_url.netloc + '/'
        short_url = domain + short_code
        with connection.cursor() as cursor:
            cursor.execute('SELECT id FROM shorturls WHERE shorturl = %s', (short_url,))
            record = cursor.fetchone()
            if not record:
                connection.close()
                return short_url


def save_url(original_url):
    short_url = generate_short_url(original_url)
    screenshot_data = get_screenshot(original_url)
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO shorturls (firsturl, shorturl) VALUES (%s, %s)',(original_url, short_url))
            connection.commit()

    except ExceptionGroup as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed !')
        return short_url, screenshot_data


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/getredirecturl', methods=['GET'])
def get_redirect_url():
    short_url = request.args.get('short_url')
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT firsturl FROM shorturls WHERE shorturl=%s", (short_url,))
            result = cursor.fetchone()
            long_url = result[0]
            return long_url

    except ExceptionGroup as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed !')

@app.route('/saveurl', methods=['POST'])
def saveurl():
    url = request.json['url']
    saved_short_url, screenshot_data = save_url(url)
    response_data = {
        'shortUrl': saved_short_url,
        'screenshot': screenshot_data
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)