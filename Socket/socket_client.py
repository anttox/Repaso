import socket
import dill as pickle

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 1936))
    server_socket.listen(1)
    print('Servidor escuchando en el puerto 1936...')

    while True:
        conn, addr = server_socket.accept()
        print(f'Conexión establecida con {addr}')
        try:
            data = conn.recv(1)
            if data == b'\x00':
                # Recibir el tamaño del código
                code_size = int.from_bytes(conn.recv(4), 'little')
                code_data = conn.recv(code_size)
                fun_code = pickle.loads(code_data)

                # Recibir el tamaño de los datos
                data_size = int.from_bytes(conn.recv(4), 'little')
                data_data = conn.recv(data_size)
                data = pickle.loads(data_data)

                # Simular procesamiento y enviar job_id
                job_id = 1234  # Esto debería ser único por trabajo
                conn.send(job_id.to_bytes(4, 'little'))

            elif data == b'\x01':
                # Cliente solicitando resultado
                job_id = int.from_bytes(conn.recv(4), 'little')
                if job_id == 1234:
                    result = {'resultado': 'éxito'}
                    result_data = pickle.dumps(result)
                    conn.send(len(result_data).to_bytes(4, 'little'))
                    conn.send(result_data)

        finally:
            conn.close()

if __name__ == '__main__':
    start_server()

