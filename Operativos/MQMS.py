#El algoritmo de Múltiples Colas (MQMS, por sus siglas en inglés) organiza los procesos en diferentes colas, cada una con su propio nivel de prioridad
from collections import deque

def calcular_mqms(procesos, quantums):
    # Ordenar procesos por tiempo de llegada para facilitar la simulación
    procesos.sort(key=lambda x: x['llegada'])

    # Crear colas para cada nivel de prioridad
    prioridades = set(p['prioridad'] for p in procesos)
    colas = {p: deque() for p in prioridades}
    tiempo_actual = 0
    tiempos_respuesta = {}
    tiempos_espera = {p['nombre']: 0 for p in procesos}

    # Función para manejar llegadas de procesos al sistema
    def manejar_llegadas(tiempo_actual, procesos, colas):
        while procesos and procesos[0]['llegada'] <= tiempo_actual:
            proceso = procesos.pop(0)
            proceso['duracion_original'] = proceso['duracion']  # Guardar la duración original al llegar
            colas[proceso['prioridad']].append(proceso)
            if proceso['nombre'] not in tiempos_respuesta:
                tiempos_respuesta[proceso['nombre']] = -1

    # Ejecución principal del algoritmo MQMS
    while any(colas.values()) or procesos:
        manejar_llegadas(tiempo_actual, procesos, colas)

        for prioridad in sorted(colas.keys(), reverse=True):  # Ejecutar más alta prioridad primero
            if colas[prioridad]:
                proceso = colas[prioridad].popleft()
                if tiempos_respuesta[proceso['nombre']] == -1:
                    tiempos_respuesta[proceso['nombre']] = tiempo_actual - proceso['llegada']

                # Ejecutar proceso por un quantum o hasta su finalización
                tiempo_ejecucion = min(quantums[prioridad], proceso['duracion'])
                tiempo_actual += tiempo_ejecucion
                proceso['duracion'] -= tiempo_ejecucion
                if proceso['duracion'] > 0:
                    colas[prioridad].append(proceso)
                else:
                    tiempos_espera[proceso['nombre']] += tiempo_actual - proceso['llegada'] - proceso['duracion_original']
                break
        else:
            tiempo_actual += 1  # Avanzar tiempo si no hay procesos listos

    # Calcular y mostrar tiempos promedios
    tiempo_espera_promedio = sum(tiempos_espera.values()) / len(tiempos_espera)
    tiempo_respuesta_promedio = sum(tiempos_respuesta.values()) / len(tiempos_respuesta)
    print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f}")
    print(f"Tiempo de respuesta promedio: {tiempo_respuesta_promedio:.2f}")

# Definición de los procesos
procesos = [
    {'nombre': 'A', 'llegada': 0, 'duracion': 10, 'prioridad': 2},
    {'nombre': 'B', 'llegada': 1, 'duracion': 20, 'prioridad': 1},
    {'nombre': 'C', 'llegada': 2, 'duracion': 5, 'prioridad': 3},
    {'nombre': 'D', 'llegada': 3, 'duracion': 8, 'prioridad': 2}
]
quantums = {1: 5, 2: 10, 3: 15}

calcular_mqms(procesos, quantums)

