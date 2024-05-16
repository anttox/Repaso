def is_prime(num):
    """
    Función auxiliar para verificar si un número es primo.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_coroutine():
    """
    Generador que produce números primos secuencialmente.
    """
    num = 2
    while True:
        if is_prime(num):
            # Yield el siguiente número primo y espera a recibir un valor
            received = yield num
            if received is not None:
                # Si se envía un valor, reiniciar la secuencia desde ese número
                num = received
        num += 1

# Código para interactuar con la corutina
generator = prime_coroutine()  # Crea la corutina
print(next(generator))  # Inicia la corutina y obtiene el primer número primo

# Obtener los siguientes números primos
print(generator.send(None))  # Continuar desde el último número primo
print(generator.send(None))  # Continuar desde el último número primo
print(generator.send(None))  # Continuar desde el último número primo

# Reiniciar la secuencia desde un número específico
print(generator.send(50))  # Comienza a buscar números primos desde 50
print(generator.send(None))  # Continuar desde el último número primo
print(generator.send(None))  # Continuar desde el último número primo

