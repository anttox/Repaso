import concurrent.futures

def add_number(number):
    print(f'Process {number}')
    return number

def main():
    numbers = range(1, 11)
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures=[executor.submit(add_number, number) for number in numbers]
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result() #block hasta que el resultado este disponible
            results.append(result)
            print(f'Resultado recibido es: {result}')
            
    total_sum = sum(results)
    print(f'Suma total de los numeros del 1 al 10 es : {total_sum}')

if __name__ == '__main__':
    main()