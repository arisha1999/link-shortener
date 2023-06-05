from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from db import connection
from utils import save_url
import atexit

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/getredirecturl', methods=['GET'])
def get_redirect_url():
    short_url = request.args.get('short_url')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT firsturl FROM shorturls WHERE shorturl=%s", (short_url,))
            result = cursor.fetchone()
            long_url = result[0]
            return long_url
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

@app.route('/saveurl', methods=['POST'])
def saveurl():
    url = request.json['url']
    saved_short_url, screenshot_data = save_url(url)
    response_data = {
        'shortUrl': saved_short_url,
        'screenshot': screenshot_data
    }
    return jsonify(response_data)

def close_connection():
    connection.close()

atexit.register(close_connection)

if __name__ == '__main__':
    app.run(debug=True)