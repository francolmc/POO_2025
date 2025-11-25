# Obtener registros o datos de una API RESTful usando requests
import requests

url = "https://rickandmortyapi.com/api/character/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Especie: {data['species']}")
else:
    print(f"Error: {response.status_code}")