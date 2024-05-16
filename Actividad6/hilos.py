import threading
import time
import random

#funcion para el ID
def thread_function(ID):
    print(f"Hilo {ID} en ejecución.")
    
    #time
    sleep_time = random.randint(1,5)
    time.sleep(sleep_time)
    
    print(f"Hilo {ID} termino despues de {sleep_time} segundos.")
    
#lista vacia para almacenr los hilos
threads =[]

#Creamos los hilos
for i in range(5):
    thread = threading.Thread(target=thread_function, args =(i,))
    threads.append(thread)
    thread.start()
    
#Espera a que todos los hilos terminen
for thread in threads:
    thread.join()
    
print("Se finalizó todos los hilos.")
    
    
