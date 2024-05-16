from concurrent.futures import ProcessPoolExecutor
import asyncio
import time
import random

# Funciones puras para manejar reservas
def add_reservation(reservations, reservation):
    """Agrega una nueva reserva a la lista de reservas de manera inmutable."""
    return reservations + [reservation]

def cancel_reservation(reservations, reservation_id):
    """Cancela una reserva por ID, inmutablemente."""
    return [res for res in reservations if res['id'] != reservation_id]

def update_reservation(reservations, reservation_id, new_details):
    """Actualiza una reserva por ID, inmutablemente."""
    return [res if res['id'] != reservation_id else {**res, **new_details} for res in reservations]

# Procesamiento de reservas usando multiprocessing
def process_booking_requests(requests): # ProcessPoolExecutor para manejar las solicitudes de reservas en paralelo
    """Procesa una lista de solicitudes de reserva concurrentemente."""
    with ProcessPoolExecutor(max_workers=4) as executor: 
        results = list(executor.map(handle_request, requests)) # handle_request pausa la ejecucion para simular el tiempo de procesamiento
    return results

def handle_request(request):
    """Maneja una solicitud individual simulando cierta lógica y tiempo de procesamiento."""
    time.sleep(random.uniform(0.1, 0.5))  # Simular tiempo de procesamiento
    return f"Processed request {request['id']} with status: {request['status']}"

# Función asincrona que maneja las reservas 
async def manage_reservations(requests):
    """Gestiona reservas asincrónicamente."""
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, process_booking_requests, requests)
    result = await future
    print(result)
# Funcion que genera solicitudes de reserva y las procesa asincrónicamente
async def simulate_requests():
    """Simula la llegada de solicitudes de reserva."""
    requests = [{'id': i, 'status': 'new'} for i in range(10)]  # Simulamos 10 solicitudes
    await manage_reservations(requests)
# DATO: Aqui se asegura que el script corra como un programa principal y no como un modulo importado
if __name__ == "__main__":
    asyncio.run(simulate_requests())
