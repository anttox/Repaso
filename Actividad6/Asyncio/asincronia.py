import aiohttp
import asyncio
import nest_asyncio

# Aplica un parche a asyncio para permitir anidamiento de bucles de eventos.
nest_asyncio.apply()

async def fetch(session, url):
    """
    Función asincrónica para realizar una petición HTTP.
    """
    async with session.get(url) as response:
        # Espera a recibir la respuesta completa y retorna el texto.
        return await response.text()

async def main():
    """
    Función principal que coordina las peticiones HTTP asincrónicas.
    """
    urls = [
        'https://api.github.com',  # GitHub API para metadatos
        'https://api.ipify.org?format=json',  # API para obtener la IP pública
        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder
    ]

    # Crear una sesión de cliente aiohttp para realizar peticiones HTTP.
    async with aiohttp.ClientSession() as session:
        # Crear una lista de tareas de fetch para cada URL.
        tasks = [fetch(session, url) for url in urls]
        # Ejecutar todas las tareas de forma asincrónica y esperar a que todas finalicen.
        responses = await asyncio.gather(*tasks)

        # Imprimir las respuestas obtenidas.
        for response in responses:
            print(response)

# Ejecutar el script en un entorno con un bucle de eventos ya en ejecución.
asyncio.run(main())

