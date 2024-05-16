#Se importan los módulos necesarios. Flask y jsonify para crear la aplicación web y manejar las respuestas JSON, y requests para realizar solicitudes HTTP al primer servicio.
from flask import Flask, jsonify
import requests

#Creamos una instacion de la aplicacion Flask
app = Flask(__name__)

#Se define una ruta /square que realiza una solicitud al primer servicio para obtener un número aleatorio, calcula su cuadrado y devuelve el resultado en formato JSON.
@app.route('/square', methods=['GET'])
def square():
    """Obtiene un número aleatorio del servicio 1 y devuelve su cuadrado."""
    # Realiza una solicitud GET al primer servicio para obtener un número aleatorio
    response = requests.get('http://localhost:5000/random')
    # Extrae el número de la respuesta JSON
    number = response.json()['number']
    # Calcula el cuadrado del número
    squared_number = number ** 2
    # Devuelve el resultado en formato JSON
    return jsonify(squared_number=squared_number)

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5001
    app.run(port=5001)

