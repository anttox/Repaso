from PIL import Image, ImageFilter
import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
import asyncio
import os

# Funciones de procesamiento de imágenes
def convert_to_grayscale(image):
    """Convierte la imagen a escala de grises."""
    return image.convert('L')

def apply_edge_detection(image):
    """Aplica detección de bordes a la imagen."""
    return image.filter(ImageFilter.FIND_EDGES)

# Decoradores
def time_it(func):
    """Decorador que mide el tiempo de ejecución de una función."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} tomó {end - start:.2f} segundos en ejecutarse.")
        return result
    return wrapper

def parallelize_image_processing(function):
    """Decorador que paraleliza el procesamiento de imágenes."""
    @wraps(function)
    def wrapper(images):
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(function, images))
        return results
    return wrapper

# Procesamiento de imágenes
@time_it
@parallelize_image_processing
def process_image(image):
    """Procesa una imagen aplicando las funciones de procesamiento."""
    grayscale_image = convert_to_grayscale(image)
    edge_detected_image = apply_edge_detection(grayscale_image)
    return edge_detected_image

# Función principal asíncrona
async def main():
    # Cargar imágenes desde el directorio 'images'
    image_dir = 'images'
    images = []
    for i in range(3):
        for ext in ['jpg', 'jpeg']:
            image_path = os.path.join(image_dir, f'image_{i}.{ext}')
            if os.path.exists(image_path):
                images.append(Image.open(image_path))
                break
        else:
            print(f"Imagen no encontrada: images/image_{i}.jpg o images/image_{i}.jpeg")
    
    if images:
        processed_images = process_image(images)
        # Aquí podrías guardar las imágenes procesadas o enviarlas a otro servicio
        print("Procesamiento de imágenes completado.")
    else:
        print("No se encontraron imágenes para procesar.")

if __name__ == "__main__":
    asyncio.run(main())

