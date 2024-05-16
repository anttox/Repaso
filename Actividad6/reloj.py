import asyncio

async def clock():
    for i in range(1, 11): #contar de 1 a 10
        print(f'{i} segundos han pasado.')
        await asyncio.sleep(1) #esperar un segundo

async def main():
    await clock() #corutina clock

if __name__ == '__main__':
    asyncio.run(main())
    
        