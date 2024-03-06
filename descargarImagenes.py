import requests

import requests

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(nombre_archivo, 'wb') as f:
                f.write(response.content)
            print(f"Imagen descargada correctamente: {nombre_archivo}")
        else:
            print(f"Error al descargar la imagen desde {url}. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al descargar la imagen desde {url}: {e}")