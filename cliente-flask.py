from flask import Flask, request, jsonify
import win32com.client

app = Flask(__name__)

# Ruta para procesar los datos financieros
@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    data = request.json['data']
    
    # Conectarse a Excel
    excel = win32com.client.Dispatch("Excel.Application")
    workbook = excel.Workbooks.Add()
    sheet = workbook.Sheets(1)
    
    # Realizar cálculos en Excel
    resultado = 0
    for i, registro in enumerate(data, start=1):
        sheet.Cells(i, 1).Value = registro['valor']
        resultado += registro['valor']  # Simula cálculo de balance total
    
    # Cerrar Excel
    workbook.Close(False)
    excel.Quit()
    
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Puerto único para cada cliente
