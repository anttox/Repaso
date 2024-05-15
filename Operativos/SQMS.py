#El algoritmo de Múltiples Colas con Retroaalimentacion es una variante avanzada del Round Robin que utiliza múltiples colas, cada una con un quantum de tiempo diferente, generalmente incrementando con cada nivel más bajo
#deque es una estructura de datos tipo cola doblemente terminada que permite agregar y remover elementos de ambos extremos con eficiencia.
from collections import deque

def calcular_mfq(procesos, quantums):
    # Inicializar colas para cada nivel
    colas = [deque() for _ in quantums]
    tiempo_actual = 0
    tiempos_respuesta = {}
    tiempos_espera = {p['nombre']: 0 for p in procesos}
    procesos.sort(key=lambda x: x['llegada'])
    indice_proceso = 0

    # Función para manejar la llegada de procesos
    def manejar_llegadas(tiempo_actual, indice_proceso, procesos, colas):
        #Agrega el proceso a la cola de nivel más alto y establece su tiempo de respuesta inicial a -1 para indicar que no ha empezado a procesarse. Incrementa el índice para procesar el siguiente proceso
        while indice_proceso < len(procesos) and procesos[indice_proceso]['llegada'] <= tiempo_actual:
            proceso = procesos[indice_proceso]
            colas[0].append(proceso)
            tiempos_respuesta[proceso['nombre']] = -1
            indice_proceso += 1
        return indice_proceso

    # Ejecución de los procesos en las colas
    # Continúa mientras haya procesos en alguna cola o procesos por llegar -> while
    while any(colas) or indice_proceso < len(procesos):
        indice_proceso = manejar_llegadas(tiempo_actual, indice_proceso, procesos, colas)
        
        #itera sobre cada cola y su nivel correspondiente
        for nivel, cola in enumerate(colas):
            if cola:
                #Extrae el primer proceso de la cola para ejecutarlo ->cola.poplef
                proceso_actual = cola.popleft()
                #Si es la primera vez que se ejecuta el proceso, registra el tiempo de respuesta
                if tiempos_respuesta[proceso_actual['nombre']] == -1:
                    tiempos_respuesta[proceso_actual['nombre']] = tiempo_actual - proceso_actual['llegada']
                
                # Ejecutar proceso por el quantum de tiempo o menos si necesita menos tiempo
                tiempo_ejecucion = min(quantums[nivel], proceso_actual['duracion'])
                tiempo_actual += tiempo_ejecucion
                proceso_actual['duracion'] -= tiempo_ejecucion

                # Verificar si el proceso ha terminado
                if proceso_actual['duracion'] > 0:
                    # Mover a la siguiente cola si no está en la última
                    siguiente_nivel = min(nivel + 1, len(colas) - 1)
                    colas[siguiente_nivel].append(proceso_actual)
                else:
                    tiempos_espera[proceso_actual['nombre']] = tiempo_actual - proceso_actual['llegada'] - proceso_actual['duracion_original']
                break
        else:
            tiempo_actual += 1  # Avanzar el tiempo si todas las colas están vacías

    # Cálculo de tiempos promedios
    tiempo_espera_promedio = sum(tiempos_espera.values()) / len(tiempos_espera)
    tiempo_respuesta_promedio = sum(tiempos_respuesta.values()) / len(tiempos_respuesta)

    print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f}")
    print(f"Tiempo de respuesta promedio: {tiempo_respuesta_promedio:.2f}")

# Definición de los procesos
procesos = [
    {'nombre': 'A', 'llegada': 0, 'duracion': 10, 'duracion_original': 10},
    {'nombre': 'B', 'llegada': 1, 'duracion': 20, 'duracion_original': 20},
    {'nombre': 'C', 'llegada': 2, 'duracion': 5, 'duracion_original': 5},
    {'nombre': 'D', 'llegada': 3, 'duracion': 8, 'duracion_original': 8}
]

# Quantums para cada cola
quantums = [4, 8, 12]

calcular_mfq(procesos, quantums)

