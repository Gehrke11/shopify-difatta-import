from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

EMAIL = os.environ.get(Info@clown-pepe.at)
PASSWORD = os.environ.get(Papa2010@)

@app.route("/products")
def get_products():
    url = "https://difattamagic.com/csvprodotti/customerapi/getinfo"
    response = requests.post(url, data={"email": EMAIL, "password": PASSWORD})
    if response.status_code == 200:
        data = response.json()
        return jsonify({"count": len(data), "products": data[:3]})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
