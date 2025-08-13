from flask import Flask, request, jsonify
import base64
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a la API de captura de pantalla'

@app.route('/captura', methods=['GET'])
def capturar_pagina():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Parámetro 'url' es obligatorio"}), 400

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1280x720')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')  # Evita errores de memoria compartida en contenedores

    # Aquí usamos webdriver-manager para manejar el chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)

    screenshot = driver.get_screenshot_as_png()
    driver.quit()

    screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')

    return jsonify({"image": screenshot_base64})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


