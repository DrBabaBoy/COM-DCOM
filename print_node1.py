# print_node1.py
import pythoncom
import time
import win32com.server.register

class PrintNode1:
    _public_methods_ = ['process_print']
    _reg_progid_ = "PrintNode1.Application"
    _reg_clsid_ = "{e1a8b3be-ff12-42e7-b91f-1234567890a1}"  # GUID único para el nodo 1

    def process_print(self, job_id, document_name, print_type, copies):
        # Construir mensaje completo
        output = f"\nNodo 1 ------\n"
        output += f"Imprimiendo el Archivo: '{document_name}', {print_type}\n"
        for i in range(copies):
            time.sleep(2)  # Simula el tiempo de impresión
            output += f"Imprimiendo el Archivo: '{document_name}', copia {i + 1} de {copies} - Nodo 1\n"
        output += "\nFinalizado\n"

        # Imprimir mensaje completo en una sola operación
        print(output)

if __name__ == '__main__':
    win32com.server.register.UseCommandLine(PrintNode1)
