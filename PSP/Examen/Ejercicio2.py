import os
import tempfile
import threading
import subprocess
import time

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
lock = threading.Lock()

def code(name):
    with lock:
        print(f"Iniciando código para {name}")
        
    time.sleep(10)
    
    with lock:
        print(f"Guardando en {file_name}")
        
    with open(file_name, 'a') as f:
        with lock:
            f.write("Código limpio fue escrito por " + str(name) + "\n")
    
    subprocess.run(["ping", "-c", "4", "google.com"])
    
    
    with lock:
        print(f"{name} ha terminado el ping")

# Crear múltiples hilos
threads = []
for i in range(3):  # Por ejemplo, 3 hilos
    thread = threading.Thread(target=code, args=(f'Hilo-{i}',))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

# Mostrar el contenido del archivo
with open(file_name, 'r') as f:
    print("\nContenido del archivo:")
    print(f.read())
