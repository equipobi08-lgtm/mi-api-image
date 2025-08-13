from flask import Flask, request, jsonify
import base64, time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a la API de captura de pantalla'

@app.route('/captura', methods=['GET'])
def capturar_pagina():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Parámetro 'url' es obligatorio"}), 400

    chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
    chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver"

    options = Options()
    options.binary_location = chrome_path
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()

    image_b64 = base64.b64encode(screenshot).decode('utf-8')
    return jsonify({"image": image_b64})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
