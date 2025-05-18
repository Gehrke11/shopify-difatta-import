import requests

# Zugangsdaten (ersetzen durch deine echten Zugangsdaten!)
EMAIL = "Info@clown-pepe.at"
PASSWORD = "Papa2010@"

# DiFatta API-URL
url = "https://difattamagic.com/csvprodotti/customerapi/getinfo"

# Anfrage senden
response = requests.post(url, data={"email": EMAIL, "password": PASSWORD})

# Antwort prüfen und ausgeben
if response.status_code == 200:
    data = response.json()
    print("Produkte empfangen:", len(data))
    print(data[:3])  # Zeige erste 3 Produkte zur Kontrolle
else:
    print("Fehler beim Abrufen:", response.status_code, response.text)
