from functools import reduce #importante para usar reduce

def to_upper(word):
    # upper -> convierte una palabra en mayuscula
    return word.upper()

def concatenate(a, b):
    # concatenar dos cadenas -> reduce
    return a + ',' + b

def main():
    words = ["hello", "world", "this", "is", "python"]
    
    # usar map para convertir todas las palabras en mayusculas
    upper_words = map(to_upper, words)
    
    # usar reduce para concatenarlas en una sola cadena 
    concatenated_string = reduce(concatenate, upper_words)
    
    print(concatenated_string)

if __name__ == "__main__":
    main()
        