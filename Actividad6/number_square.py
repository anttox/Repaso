import multiprocessing 

def f(x): #calcular el cuadrado de un numero
    return x*x

def main():
    x = range(1, 11)
    #creamos un Pool de procesos
    with multiprocessing.Pool() as pool:
        squares = pool.map(f, x)
        
    print("Cuadrados de los numeros del 1 al 10:")
    for x, square in zip(x, squares):
        print(f'El cuadrado de {x} es {square}')
if __name__ == '__main__':
    main()
        