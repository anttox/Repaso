import multiprocessing

#factorial

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return (numero, factorial)

#paralelismo    
def map_test():
    pool = multiprocessing.Pool()
    
    inputs = [5, 7, 9]
    ouputs = pool.map(calcular_factorial, inputs)
    print(ouputs)

map_test()

    

