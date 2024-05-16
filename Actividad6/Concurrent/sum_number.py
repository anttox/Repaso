import concurrent.futures

def sum_range(start, end):
    """
    Suma todos los números en el rango dado, incluyendo el inicio y el fin.
    
    Args:
        start (int): El número de inicio del rango.
        end (int): El número final del rango.
    
    Returns:
        int: La suma de todos los números en el rango.
    """
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

def main():
    """
    Divide el rango de números del 1 al 10 en tres partes y suma cada parte en un hilo separado.
    Luego, suma los resultados parciales para obtener la suma total.
    """
    ranges = [(1, 3), (4, 6), (7, 10)]  # Dividiendo el rango de números en tres partes.
    results = []
    
    # Usando ThreadPoolExecutor para manejar múltiples hilos
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Crear futuros para cada rango de sumas.
        futures = [executor.submit(sum_range, r[0], r[1]) for r in ranges]
        
        # Recopilar los resultados a medida que se completan.
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(f"Resultado obtenido: {result}")
            results.append(result)
    
    # Sumar los resultados parciales para obtener el total final.
    total_sum = sum(results)
    print(f"La suma total de 1 a 10 es: {total_sum}")

if __name__ == "__main__":
    main()

