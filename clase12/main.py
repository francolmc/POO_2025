import json
import requests

usuario = {
    "name": "Juan",
    "username": "juan123",
    "email": "juan@example.com"
}

usuario_json = json.dumps(usuario)

post_url = "https://jsonplaceholder.typicode.com/users"

post_response = requests.post(post_url, data=usuario_json, headers={"Content-Type": "application/json"})

if post_response.status_code == 201:
    print("Usuario creado exitosamente:")
    print(post_response.json())
else:
    print(f"Error al crear usuario: {post_response.status_code}")


