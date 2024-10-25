# server_app.py
import pythoncom
import win32com.client
import uuid
import queue
import threading
import time
from flask import Flask, request, jsonify

app = Flask(__name__)
jobs = {}
node_queues = {1: queue.Queue(), 2: queue.Queue(), 3: queue.Queue()}
node_loads = {1: 0, 2: 0, 3: 0}
lock = threading.Lock()

@app.route('/upload', methods=['POST'])
def upload_document():
    document_name = request.form['document_name']
    print_type = request.form['print_type']
    copies = int(request.form['copies'])
    job_id = str(uuid.uuid4())

    with lock:
        available_node = min(node_loads, key=node_loads.get)
        node_queues[available_node].put((job_id, document_name, print_type, copies))
        node_loads[available_node] += 1

    jobs[job_id] = {'status': 'En cola', 'document_name': document_name, 'remaining_copies': copies, 'node_id': available_node}

    if node_queues[available_node].qsize() == 1:
        threading.Thread(target=process_node_queue, args=(available_node,)).start()
    
    return jsonify({'job_id': job_id, 'status': 'En cola'}), 200

@app.route('/job_status/<job_id>', methods=['GET'])
def job_status(job_id):
    job_info = jobs.get(job_id, {'status': 'No encontrado', 'document_name': 'Desconocido', 'remaining_copies': 0, 'node_id': 'Desconocido'})
    return jsonify(job_info), 200

def process_node_queue(node_id):
    pythoncom.CoInitialize()
    node_prog_id = f"PrintNode{node_id}.Application"
    try:
        node = win32com.client.Dispatch(node_prog_id)
        
        while not node_queues[node_id].empty():
            job_id, document_name, print_type, copies = node_queues[node_id].get()
            jobs[job_id]['status'] = 'En proceso'
            jobs[job_id]['node_id'] = node_id
            
            for i in range(copies):
                node.process_print(job_id, document_name, print_type, i + 1)
                with lock:
                    jobs[job_id]['remaining_copies'] -= 1
                time.sleep(2)

            with lock:
                jobs[job_id]['status'] = "Completado"
                node_loads[node_id] -= 1
    except Exception as e:
        print(f"Error procesando trabajo en Nodo {node_id}: {e}")
    finally:
        pythoncom.CoUninitialize()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)