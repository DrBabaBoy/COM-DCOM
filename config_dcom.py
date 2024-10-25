# config_dcom.py
import os
import subprocess

def configure_dcom():
    print("Configurando permisos de DCOM para el sistema...")

    try:
        # Configuración de reglas de firewall para permitir DCOM
        subprocess.call(["powershell", 
                         "New-NetFirewallRule -DisplayName 'Allow DCOM' -Direction Inbound -Protocol TCP -LocalPort 135 -Action Allow"])
        print("Permisos de DCOM configurados exitosamente.")
    except Exception as e:
        print(f"Error configurando DCOM: {e}")

if __name__ == "__main__":
    configure_dcom()
