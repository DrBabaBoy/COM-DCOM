# start_system.py
import subprocess
import time

def start_server():
    return subprocess.Popen(["python", "server_app.py"])

def start_node(node_file):
    return subprocess.Popen(["python", node_file])

def start_client():
    return subprocess.Popen(["python", "client_app.py"])

if __name__ == "__main__":
    server_process = start_server()
    time.sleep(2)
    node_files = ["print_node1.py", "print_node2.py", "print_node3.py"]
    node_processes = [start_node(node_file) for node_file in node_files]
    client_process = start_client()

    try:
        server_process.wait()
        for process in node_processes:
            process.wait()
        client_process.wait()
    except KeyboardInterrupt:
        server_process.terminate()
        for process in node_processes:
            process.terminate()
        client_process.terminate()
