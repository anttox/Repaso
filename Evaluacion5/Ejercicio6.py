from concurrent.futures import ThreadPoolExecutor
import asyncio

# Funciones puras para calcular indicadores financieros
# Comprueba si hay suficientes precios para calcular la media movi sino retorna None
# Calcula y retorna la media movil simple utilizando los ultimos window_size precios
def calculate_moving_average(prices, window_size=20):
    """Calcula la media móvil simple de los precios."""
    if len(prices) < window_size:
        return None  # No hay suficientes datos para calcular la media móvil
    return sum(prices[-window_size:]) / window_size
# Calcula las ganancias y perdidas diarias
def calculate_rsi(prices, periods=14):
    """Calcula el índice de fuerza relativa (RSI) para una lista de precios."""
    if len(prices) < periods:
        return None  # No hay suficientes datos para calcular el RSI

    gains = [max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices))]
    losses = [max(0, prices[i - 1] - prices[i]) for i in range(1, len(prices))]

    average_gain = sum(gains[-periods:]) / periods
    average_loss = sum(losses[-periods:]) / periods

    if average_loss == 0:
        return 100  # Evitar división por cero
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Análisis paralelo de datos bursátiles
def parallel_analyze_data(stock_data):
    """Analiza datos bursátiles en paralelo utilizando múltiples hilos."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(analyze_stock, stock_data))
    return results

# Procesa los datos de un solo stock calculando la media movil y el RSI
def analyze_stock(data):
    """Analiza los datos de un solo stock."""
    moving_average = calculate_moving_average(data['prices'])
    rsi = calculate_rsi(data['prices'])
    return {'stock': data['stock'], 'moving_average': moving_average, 'RSI': rsi}

# Función asincrónica para simular la recepción de datos bursátiles en tiempo real
async def stream_stock_data():
    """Simula la recepción de datos bursátiles en tiempo real."""
    example_data = [
        {'stock': 'AAPL', 'prices': [150, 151, 152, 153, 154]},
        {'stock': 'GOOGL', 'prices': [1200, 1202, 1204, 1206, 1208]}
    ]
    while True:
        await asyncio.sleep(1)  # Simular la recepción de datos cada segundo
        processed_data = await asyncio.get_event_loop().run_in_executor(None, parallel_analyze_data, example_data)
        print("Processed Data:", processed_data)

if __name__ == "__main__":
    asyncio.run(stream_stock_data())
