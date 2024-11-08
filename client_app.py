from flask import Flask, render_template, request, redirect, url_for
import requests
import logging
import os

# Configuración para reducir el nivel de registro de werkzeug
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print', methods=['POST'])
def print_document():
    document_name = request.form['document']
    print_type = request.form['print_type']
    copies = request.form['copies']
    file = request.files['file']
    
    # Guardar el archivo temporalmente
    file_path = f"temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)
    file.save(file_path)
    
    # Enviar la solicitud al servidor
    with open(file_path, 'rb') as f:
        response = requests.post('http://localhost:5001/upload', data={
            'document_name': document_name,
            'print_type': print_type,
            'copies': copies
        }, files={'file': f})

    job_id = response.json().get('job_id')
    return redirect(url_for('status', job_id=job_id))

@app.route('/status/<job_id>')
def status(job_id):
    response = requests.get(f'http://localhost:5001/job_status/{job_id}')
    job_info = response.json()
    return render_template('status.html', job_info=job_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=False)
