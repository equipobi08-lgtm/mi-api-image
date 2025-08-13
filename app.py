from flask import Flask, request, jsonify
import base64
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a la API de captura de pantalla'

@app.route('/captura', methods=['GET'])
def capturar_pagina():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Parámetro 'url' es obligatorio"}), 400

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        screenshot = page.screenshot()
        browser.close()

    screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
    return jsonify({"image": screenshot_base64})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



