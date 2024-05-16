import nltk
nltk.download('stopwords')
nltk.download('punkt')
#import re: Se utiliza para manipular textos mediante expresiones regulares, en este caso, para limpiar el texto eliminando caracteres no alfanuméricos mediante la función re.sub
import re
import asyncio
#from nltk.corpus import stopwords: Importa la lista de palabras vacías (stopwords) del módulo nltk, que es una biblioteca de procesamiento de lenguaje natural.
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize: Esta función se usa para dividir cadenas de texto en listas de palabras o "tokens". Es esencial para procesar y analizar el texto correctamente, particularmente para la eliminación de stopwords.
from nltk.tokenize import word_tokenize
#TextBlob es utilizada para realizar tareas comunes de procesamiento de lenguaje natural, incluyendo análisis de sentimientos. Esta biblioteca proporciona una interfaz sencilla para obtener la polaridad y subjetividad de los textos, lo cual indica el sentimiento general y el grado de objetividad o subjetividad.
from textblob import TextBlob
from concurrent.futures import ThreadPoolExecutor

# Inicializar la lista de stopwords
stop_words = set(stopwords.words('english'))

# Funciones puras para pre-procesamiento de textos
def clean_text(text):
    """Limpia el texto eliminando caracteres especiales y convirtiéndolo a minúsculas."""
    text = re.sub(r'\W', ' ', text)  # Elimina caracteres no alfanuméricos
    text = text.lower()  # Convierte el texto a minúsculas
    return text

def remove_stopwords(text):
    """Elimina las stopwords de un texto."""
    words = word_tokenize(text)  # Tokeniza el texto
    filtered_words = [word for word in words if word not in stop_words]  # Filtra las stopwords
    return ' '.join(filtered_words)  # Une las palabras filtradas en una cadena

def preprocess_text(text):
    """Combina todas las operaciones de preprocesamiento de texto."""
    text = clean_text(text)  # Limpia el texto
    text = remove_stopwords(text)  # Elimina stopwords
    return text

# Análisis de sentimiento utilizando TextBlob
def analyze_sentiment(text):
    """Analiza el sentimiento de un texto dado y devuelve el resultado."""
    analysis = TextBlob(text)
    return analysis.sentiment  # Devuelve la polaridad y subjetividad

# Análisis concurrente de textos
def analyze_texts_concurrently(texts):
    """Analiza una lista de textos concurrentemente."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(preprocess_and_analyze, texts))  # Procesa y analiza textos en paralelo
    return results

def preprocess_and_analyze(text):
    """Preprocesa y analiza el sentimiento de un texto."""
    preprocessed_text = preprocess_text(text)  # Preprocesa el texto
    sentiment = analyze_sentiment(preprocessed_text)  # Analiza el sentimiento
    return sentiment

# Manejo asíncrono de datos
async def collect_and_process_data(stream_data):
    """Asíncronamente recolecta y procesa datos de un flujo."""
    processed_data = await asyncio.get_event_loop().run_in_executor(None, analyze_texts_concurrently, stream_data)
    print("Sentiment Analysis Results:", processed_data)

async def simulate_streaming_data():
    """Simula la llegada de datos de texto de un flujo en tiempo real."""
    sample_data = [
        "I love this product!",
        "This is the worst service ever.",
        "I'm not sure if I like this.",
        "Absolutely fantastic!"
    ]
    await collect_and_process_data(sample_data)  # Procesa los datos simulados

if __name__ == "__main__":
    asyncio.run(simulate_streaming_data())  # Inicia la simulación
