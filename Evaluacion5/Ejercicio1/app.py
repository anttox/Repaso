from flask import Flask, request, jsonify
from PIL import Image, UnidentifiedImageError
import io
from image_processing import process_image  # Asegúrate de que este import sea correcto

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    try:
        image = Image.open(io.BytesIO(file.read()))
    except UnidentifiedImageError:
        return jsonify({"error": "El archivo cargado no es una imagen válida"}), 400
    
    processed_image = process_image([image])[0]
    byte_arr = io.BytesIO()
    processed_image.save(byte_arr, format='JPEG')
    return jsonify({"processed_image": byte_arr.getvalue().hex()})

if __name__ == '__main__':
    app.run(debug=True)

