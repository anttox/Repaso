#concurrent.futures: Proporciona una interfaz de alto nivel para la ejecución asíncrona de llamadas.
import concurrent.futures
#subprocess: Permite ejecutar nuevos programas y capturar sus salidas.
import subprocess

def execute_command(command):
    """
    Ejecuta un comando del sistema y retorna la salida.
    
    Parameters:
    command (str): El comando del sistema operativo a ejecutar.
    
    Returns:
    tuple: Una tupla que contiene el comando, la salida estándar y el código de retorno.
    """
    try:
        # Ejecutar el comando y capturar la salida estándar y el error estándar
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return (command, result.stdout, result.returncode)
    except subprocess.CalledProcessError as e:
        # En caso de error en la ejecución del comando
        return (command, e.output, e.returncode)

def main(commands):
    """
    Función principal para ejecutar comandos en paralelo.
    
    Parameters:
    commands (list): Una lista de comandos del sistema operativo a ejecutar.
    """
    # Usar ThreadPoolExecutor para gestionar un grupo de threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Mapear los comandos a la función execute_command y ejecutarlos en paralelo
        results = list(executor.map(execute_command, commands))

        # Procesar los resultados
        for command, output, returncode in results:
            if returncode == 0:
                print(f"Command: {command}\nOutput: {output}\n")
            else:
                print(f"Command: {command}\nError: {output}\nReturn Code: {returncode}\n")

if __name__ == "__main__":
    # Lista de comandos del sistema para ejecutar
    commands = [
        'echo Hello, World!',
        'ls -la',
        'pwd',
        'invalid_command'
    ]
    
    main(commands)

