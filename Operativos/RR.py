#Round robin es esencialmente un sistema de tiempo compartido que asigna a cada proceso un pequeño intervalo de tiempo llamado quantum, después del cual el proceso es interrumpido y enviado al final de la cola de espera si aún necesita más tiempo de CPU
def calcular_round_robin(procesos, quantum):
    from collections import deque

    # Preparar la cola de procesos
    cola = deque()
    tiempo_actual = 0
    tiempos_respuesta = {}
    tiempos_espera = {p['nombre']: 0 for p in procesos}

    # Agregar procesos a la cola en el orden de llegada
    procesos.sort(key=lambda x: x['llegada'])
    indice_proceso = 0

    while indice_proceso < len(procesos) or cola:
        # Agregar procesos que han llegado al tiempo actual
        while indice_proceso < len(procesos) and procesos[indice_proceso]['llegada'] <= tiempo_actual:
            proceso = procesos[indice_proceso]
            cola.append(proceso)
            tiempos_respuesta[proceso['nombre']] = -1
            indice_proceso += 1

        if cola:
            proceso_actual = cola.popleft()
            # Registrar el inicio de la respuesta si es la primera vez que se ejecuta
            if tiempos_respuesta[proceso_actual['nombre']] == -1:
                tiempos_respuesta[proceso_actual['nombre']] = tiempo_actual - proceso_actual['llegada']

            # Calcular la duración de ejecución para este turno
            duracion = min(quantum, proceso_actual['duracion'])
            tiempo_actual += duracion
            proceso_actual['duracion'] -= duracion

            # Revisar si el proceso necesita más tiempo
            if proceso_actual['duracion'] > 0:
                cola.append(proceso_actual)
                # Actualizar el tiempo de espera para otros procesos en la cola
                for proc in cola:
                    if proc['nombre'] != proceso_actual['nombre']:
                        tiempos_espera[proc['nombre']] += duracion
            else:
                # Proceso termina
                tiempos_espera[proceso_actual['nombre']] += tiempo_actual - proceso_actual['llegada'] - proceso_actual['duracion_original']

        else:
            tiempo_actual += 1  # Avanzar el tiempo si la cola está vacía

    # Calcular tiempos finales de espera y respuesta
    tiempo_espera_promedio = sum(tiempos_espera.values()) / len(tiempos_espera)
    tiempo_respuesta_promedio = sum(tiempos_respuesta.values()) / len(tiempos_respuesta)

    print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f}")
    print(f"Tiempo de respuesta promedio: {tiempo_respuesta_promedio:.2f}")

# Definición de los procesos
procesos = [
    {'nombre': 'A', 'llegada': 0, 'duracion': 10, 'duracion_original': 10},
    {'nombre': 'B', 'llegada': 1, 'duracion': 4, 'duracion_original': 4},
    {'nombre': 'C', 'llegada': 2, 'duracion': 5, 'duracion_original': 5},
    {'nombre': 'D', 'llegada': 3, 'duracion': 3, 'duracion_original': 3}
]

calcular_round_robin(procesos, quantum=4)

