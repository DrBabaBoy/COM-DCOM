# print_node3.py
import pythoncom
import time
import win32com.server.register

class PrintNode3:
    _public_methods_ = ['process_print']
    _reg_progid_ = "PrintNode3.Application"
    _reg_clsid_ = "{e3c8b3be-ff12-42e7-b91f-1234567890c3}"  # GUID único para el nodo 3

    def process_print(self, job_id, document_name, print_type, copies):
        # Construir mensaje completo
        output = f"\nNodo 3 ------\n"
        output += f"Imprimiendo el Archivo: '{document_name}', {print_type}\n"
        for i in range(copies):
            time.sleep(2)  # Simula el tiempo de impresión
            output += f"Imprimiendo el Archivo: '{document_name}', copia {i + 1} de {copies} - Nodo 3\n"
        output += "\nFinalizado\n"

        # Imprimir mensaje completo en una sola operación
        print(output)

if __name__ == '__main__':
    win32com.server.register.UseCommandLine(PrintNode3)
