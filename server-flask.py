from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ruta para distribuir el trabajo a los clientes
@app.route('/distribuir_tareas', methods=['POST'])
def distribuir_tareas():
    data = request.json['data']  # Datos financieros
    clientes = request.json['clientes']  # Lista de URLs de clientes
    resultados = []
    
    # Divide el trabajo y envía a cada cliente
    for i, cliente in enumerate(clientes):
        subset = data[i::len(clientes)]  # División de datos
        response = requests.post(f"{cliente}/procesar_datos", json={"data": subset})
        resultados.append(response.json())

    # Consolidar resultados
    total = sum(res["resultado"] for res in resultados)
    return jsonify({"total_balance": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
