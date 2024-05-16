from concurrent.futures import ProcessPoolExecutor
import asyncio

# Definición de funciones puras para análisis de datos
def calculate_average_speed(speeds):
    """Calcula la velocidad promedio a partir de una lista de velocidades."""
    total_speed = sum(speeds)
    count = len(speeds)
    return total_speed / count if count else 0

def calculate_traffic_volume(vehicles):
    """Calcula el volumen de tráfico a partir de una lista de conteos de vehículos."""
    return sum(vehicles)

# Uso de concurrent.futures para paralelizar el procesamiento de datos
def process_traffic_data(locations_data): #ProcessPoolExecutor para procesar datos de multiples ubicaciones en paralelo
    """Procesa datos de múltiples ubicaciones utilizando procesamiento en paralelo."""
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_single_location, locations_data))
    return results

def process_single_location(location_data):
    """Procesa los datos de tráfico de una única ubicación."""
    average_speed = calculate_average_speed(location_data['speed'])
    traffic_volume = calculate_traffic_volume(location_data['vehicles'])
    return {'location': location_data['location'], 'average_speed': average_speed, 'traffic_volume': traffic_volume}

# Integración con asyncio para manejo asíncrono
async def update_traffic_data(): #Funcion asincrona que se ejecuta continuamente para actualizar los datos y la visualizacion
    """Actualiza periódicamente los datos de tráfico y la visualización."""
    while True:
        locations_data = fetch_traffic_data()
        processed_data = await asyncio.get_event_loop().run_in_executor(None, process_traffic_data, locations_data)
        update_visualization(processed_data)
        await asyncio.sleep(10)  # Actualiza cada 10 segundos

# Funcion que simula la recoleccion de datos de trafico desde sensores o APIs
def fetch_traffic_data(): 
    """Simula la recolección de datos de tráfico de múltiples sensores."""
    return [{'location': 'Location A', 'speed': [40, 50, 55], 'vehicles': [100, 120, 130]},
            {'location': 'Location B', 'speed': [30, 35, 40], 'vehicles': [90, 110, 115]}]

# Funcion que actualiza la interfaz de usuario o dashboard con los datos procesados
def update_visualization(data):
    """Actualiza una interfaz de usuario o un dashboard con los últimos datos procesados."""
    print("Updated visualization with:", data)

if __name__ == "__main__":
    asyncio.run(update_traffic_data())
