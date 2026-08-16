import requests

def obtener_datos(post_id=1):
    # Usamos una f-string para que la URL sea dinámica y acepte diferentes IDs
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    respuesta = requests.get(url)
    return respuesta.json()