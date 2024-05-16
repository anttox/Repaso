#Programacion distribuida
import concurrent.futures

def fibonacci(n):
    """ Calcula el n-ésimo número de Fibonacci. """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    # Lista de números para los cuales calcular la serie Fibonacci
    nums = [10, 20, 30, 35, 40]
    
    # Usar ThreadPoolExecutor para calcular los números de Fibonacci de forma concurrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Usamos map para aplicar la función a cada elemento en nums
        results = executor.map(fibonacci, nums)
        
        # Imprimir resultados
        for num, result in zip(nums, results):
            print(f'Fibonacci({num}) = {result}')

if __name__ == "__main__":
    main()
