#Metodo de planificación de procesos donde el proceso con el tiempo de ejecución más corto es seleccionado para ejecución en primer lugar
procesos = [
    {'nombre': 'A', 'llegada': 0, 'duracion': 5},
    {'nombre': 'B', 'llegada': 2, 'duracion': 3},
    {'nombre': 'C', 'llegada': 4, 'duracion': 1},
    {'nombre': 'D', 'llegada': 6, 'duracion': 2}
]

def calcular_sjf(procesos):
    procesos.sort(key=lambda x: (x['llegada'], x['duracion']))

    tiempo_actual = 0
    tiempos_espera = []
    tiempos_respuesta = []
    cola_procesos = []
    procesos_terminados = []
    
    #El codigo revisara si algun proceso ha llegado al tiempo actual y lo añade a la cola de procesos
    while procesos or cola_procesos:
        while procesos and procesos[0]['llegada'] <= tiempo_actual:
            cola_procesos.append(procesos.pop(0))
        #Los procesos en la cola se ordenan para ejecutar el mas corto disponible
        cola_procesos.sort(key=lambda x: x['duracion'])
        if cola_procesos:
            proceso_actual = cola_procesos.pop(0)
            tiempo_espera = tiempo_actual - proceso_actual['llegada']
            tiempos_espera.append(tiempo_espera)
            tiempo_inicio = tiempo_actual
            tiempo_actual += proceso_actual['duracion']
            tiempo_fin = tiempo_actual
            tiempos_respuesta.append(tiempo_fin - proceso_actual['llegada'])
            procesos_terminados.append(proceso_actual['nombre'])

            print(f"Proceso {proceso_actual['nombre']}: Inicia = {tiempo_inicio}, Finaliza = {tiempo_fin}, Espera = {tiempo_espera}")
        else:
            tiempo_actual += 1  # Avanzar el tiempo si la cola está vacía

    # Calcular y mostrar los tiempos promedio
    tiempo_espera_promedio = sum(tiempos_espera) / len(tiempos_espera)
    tiempo_respuesta_promedio = sum(tiempos_respuesta) / len(tiempos_respuesta)
    print(f"Orden de ejecución: {' -> '.join(procesos_terminados)}")
    print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f}")
    print(f"Tiempo de respuesta promedio: {tiempo_respuesta_promedio:.2f}")

calcular_sjf(procesos)
