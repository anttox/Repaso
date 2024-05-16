import requests
from concurrent.futures import ThreadPoolExecutor
import os

# URLs actualizadas de las imágenes que deseamos descargar
image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Lake_mapourika_NZ.jpeg/320px-Lake_mapourika_NZ.jpeg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/220px-June_odd-eyed-cat.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Australien-Krokodil.JPG/1024px-Australien-Krokodil.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/d/dd/Scarlet_Macaw_and_Blue-and-gold_Macaw.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/09/Polar_Bear_-_Alaska.jpg"
]

def download_image(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Descarga completada: {filename}")
        else:
            print(f"Error al descargar {filename}, HTTP {response.status_code}")
    except Exception as e:
        print(f"No se pudo descargar {filename}. Error: {str(e)}")

folder = "downloaded_images"
os.makedirs(folder, exist_ok=True)

with ThreadPoolExecutor(max_workers=5) as executor:
    for url in image_urls:
        filename = os.path.join(folder, url.split('/')[-1])
        executor.submit(download_image, url, filename)

print("Todas las descargas han sido completadas.")

