#El uso de await en Python se utiliza dentro de funciones definidas con async def. 
#Este permite que la función espere de manera asíncrona la finalización de una operación sin bloquear la ejecución del programa.
import asyncio

# Define una función asíncrona para simular la descarga de un archivo.
async def download_file(file_name, duration):
    print(f"Inicio de la descarga {file_name}")
    
    # La función asyncio.sleep() se usa para simular una espera no bloqueante.
    await asyncio.sleep(duration)
    print(f"Descarga completada de {file_name} despues de {duration} segundos")

# Define la función principal que coordina las descargas.
async def main():
    # Crea una lista de tareas de descarga, cada una con un nombre de archivo y una duración específica.
    downloads = [
        download_file("file1.txt", 3),
        download_file("file2.txt", 5),
        download_file("file3.txt", 7)
    ]
    
    # Usa asyncio.gather() para ejecutar todas las tareas de descarga de manera concurrente.
    await asyncio.gather(*downloads)

# Ejecuta la función principal en el bucle de eventos de asyncio.
asyncio.run(main())
