#Los procesos llegan en diferentes momentos y tienen diferentes duraciones. First-Come, First-Served (FCFS) para determinar el orden de ejecución y el tiempo de espera promedio
#Definir procesos
procesos = [
        {'nombre':'A', 'llegada': 0, 'duracion':3},
        {'nombre':'B', 'llegada': 2, 'duracion':6},
        {'nombre':'C', 'llegada': 4, 'duracion':4}
]

#Ordenar procesos usando sort
procesos.sort(key=lambda x: x['llegada'])

#Calculamos el tiempo de inicio, fin y espera
tiempo_actual = 0
tiempos_espera =[]

for proceso in procesos:
    #Comprobamos si el sistema debe esperar a que llegue el proximo proceso
    if tiempo_actual < proceso['llegada']:
        tiempo_actual = proceso['llegada']
    tiempo_inicio = tiempo_actual
    tiempo_fin = tiempo_inicio + proceso['duracion']
    tiempo_espera = tiempo_inicio - proceso['llegada']
    tiempos_espera.append(tiempo_espera)
    tiempo_actual = tiempo_fin

    print(f"Proceso {proceso['nombre']}: Inicia = {tiempo_inicio}, Finaliza = {tiempo_fin}, Espera = {tiempo_espera}")


