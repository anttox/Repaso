import asyncio

async def download_file(file_name, duration):
    print(f"Inicio de la descarga {file_name}")
    
    await asyncio.sleep(duration)
    print(f"Descarga completada de {file_name} despues de {duration} segundos")
    
async def main():
    
    downloads = [download_file("file1.txt", 3),
                 download_file("file2.txt", 5),
                 download_file("file3.txt", 7)
    ]
    
    await asyncio.gather(*downloads)
    
asyncio.run(main())
