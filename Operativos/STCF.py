#STCF decide en tiempo real cuál proceso ejecutar basándose en el tiempo restante más corto para completarse
def calcular_stcf(procesos):
    tiempo_actual = 0
    procesos_terminados = []
    cola_procesos = []
    ultimo_proceso = None
    tiempo_espera = {p['nombre']: 0 for p in procesos}

    # Agregar los procesos a una cola en orden de llegada
    procesos.sort(key=lambda x: x['llegada'])

    while procesos or cola_procesos:
        # Agregar nuevos procesos a la cola
        while procesos and procesos[0]['llegada'] <= tiempo_actual:
            nuevo_proceso = procesos.pop(0)
            cola_procesos.append(nuevo_proceso)
            if ultimo_proceso and ultimo_proceso['nombre'] not in procesos_terminados:
                cola_procesos.append(ultimo_proceso)

        # Ordenar la cola por tiempo restante
        cola_procesos.sort(key=lambda x: x['duracion'])

        if cola_procesos:
            proceso_actual = cola_procesos.pop(0)
            # Continuar con el proceso actual o cambiar al siguiente proceso
            if ultimo_proceso and proceso_actual['nombre'] == ultimo_proceso['nombre']:
                tiempo_actual += 1
                proceso_actual['duracion'] -= 1
            else:
                ultimo_proceso = proceso_actual
                tiempo_actual += 1
                proceso_actual['duracion'] -= 1
                tiempo_espera[proceso_actual['nombre']] += tiempo_actual - proceso_actual['llegada'] - 1

            # Finalizar proceso si se completa
            if proceso_actual['duracion'] == 0:
                procesos_terminados.append(proceso_actual['nombre'])
            else:
                cola_procesos.append(proceso_actual)
        else:
            tiempo_actual += 1  # Avanzar el tiempo si la cola está vacía

    # Calcular el tiempo de espera promedio
    tiempo_espera_promedio = sum(tiempo_espera.values()) / len(tiempo_espera)
    print(f"Orden de ejecución: {' -> '.join(procesos_terminados)}")
    print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f}")

# Definición de los procesos
procesos = [
    {'nombre': 'A', 'llegada': 0, 'duracion': 8},
    {'nombre': 'B', 'llegada': 1, 'duracion': 4},
    {'nombre': 'C', 'llegada': 2, 'duracion': 9},
    {'nombre': 'D', 'llegada': 3, 'duracion': 5}
]

calcular_stcf(procesos)

