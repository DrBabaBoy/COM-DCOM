import pythoncom
import time
import os
from PIL import Image

class PrintNode1:
    _public_methods_ = ['process_print']
    _reg_progid_ = "PrintNode1.Application"
    _reg_clsid_ = "{e1a8b3be-ff12-42e7-b91f-1234567890a1}"

    def save_file_locally(self, file_path):
        # Crea la carpeta de almacenamiento
        os.makedirs("uploads", exist_ok=True)
        # Guarda el archivo en la carpeta "uploads"
        saved_path = os.path.join("uploads", os.path.basename(file_path))
        with open(file_path, "rb") as src_file:
            with open(saved_path, "wb") as dest_file:
                dest_file.write(src_file.read())
        print(f"Archivo '{file_path}' almacenado en '{saved_path}'.")

    def process_print(self, job_id, document_name, print_type, copies, file_path):
        try:
            # Guarda el archivo en local
            self.save_file_locally(file_path)

            # Simulación de impresión
            for i in range(copies):
                time.sleep(2)
                print(f"Imprimiendo el Archivo: '{document_name}', copia {i + 1} de {copies} - Nodo 1")

            print(f"\tArchivo: '{document_name}' Finalizado - Nodo 1")

        except Exception as e:
            print(f"Error en Nodo 1 durante la impresión: {e}")

if __name__ == '__main__':
    import win32com.server.register
    win32com.server.register.UseCommandLine(PrintNode1)
