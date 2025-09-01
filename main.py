from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def recibir():
    datos = request.get_json()
    print("Datos recibidos:", datos)
    return jsonify({"status": "ok", "mensaje": "Datos recibidos"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # usa el puerto 5000 por defecto o el que te dé Railway
    app.run(host='0.0.0.0', port=port)

