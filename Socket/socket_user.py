import dill as pickle
import socket
from time import sleep

def my_funs():
    def mapper(v):
        return v, 1

    def reducer(my_args):
        v, obs = my_args
        return v, sum(obs)
    return mapper, reducer

def do_request(my_funs, data):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))  # Crear una conexión de socket al localhost en el puerto 1936
        conn.send(b'\x00')  # Enviar un byte nulo al servidor
        my_code = pickle.dumps(my_funs.__code__)  # Serializar el código de las funciones con dill
        conn.send(len(my_code).to_bytes(4, 'little', signed=False))  # Enviar la longitud del código serializado en 4 bytes (little-endian)
        conn.send(my_code)  # Enviar el código serializado
        my_data = pickle.dumps(data)  # Serializar los datos con dill
        conn.send(len(my_data).to_bytes(4, 'little'))  # Enviar la longitud de los datos serializados en 4 bytes (little-endian)
        conn.send(my_data)  # Enviar los datos serializados
        job_id = int.from_bytes(conn.recv(4), 'little')  # Recibir un entero de 4 bytes del servidor (job_id)
        print(f'Obteniendo datos desde job_id {job_id}')
    finally:
        if conn:  # Verificar si la conexión se estableció correctamente
            conn.close()  # Cerrar la conexión

    result = None
    while result is None:  # Bucle para obtener el resultado
        try:
            conn = socket.create_connection(('127.0.0.1', 1936))  # Reconectar al servidor
            conn.send(b'\x01')  # Enviar un byte de señalización al servidor
            conn.send(job_id.to_bytes(4, 'little'))  # Enviar el job_id al servidor
            result_size = int.from_bytes(conn.recv(4), 'little')  # Recibir la longitud del resultado en 4 bytes (little-endian)
            result = pickle.loads(conn.recv(result_size))  # Recibir y deserializar el resultado
        finally:
            if conn:  # Verificar si la conexión se estableció correctamente
                conn.close()  # Cerrar la conexión
        sleep(1)  # Pausar por 1 segundo antes de intentar de nuevo si el resultado no está listo
    print(f'El resultado es {result}')

if __name__ == '__main__':
    do_request(my_funs, 'Python rocks. Python es lo maximo'.split(' '))

