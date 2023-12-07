import os
import psutil
import time
import subprocess
import multiprocessing
global PROCESO_PADRE_PID
def listar_procesos():
    print("Listado de procesos:")
    for proceso in psutil.process_iter(['pid', 'name', 'status']):
        if proceso.info['name'] == "python3.exe" :
           print(f"PID: {proceso.info['pid']}, Nombre: {proceso.info['name']}, Estado: {proceso.info['status']}")
        

def proceso1(PROCESO_PADRE_PID):
    print(f"Proceso1 con PID: {os.getpid()} creado.")
    time.sleep(10) # El primer proceso vive 10 segundos
    # Enviar señal para terminar el proceso2
    for proceso in psutil.process_iter(['pid','name']):
        if proceso.info['name'] == "proceso2":
          proceso.info['pid'].terminate()

    # Evitar bucle infinito al realizar el fork a sí mismo
    if os.getppid() == PROCESO_PADRE_PID:
        # Realizar un fork de sí mismo
        print(PROCESO_PADRE_PID, os.getpid())
        process= multiprocessing.Process(name="proceso1",target=proceso1, args=(PROCESO_PADRE_PID, ))
        

def proceso2():
    print(f"Proceso2 con PID: {os.getpid()} creado.")
    time.sleep(5)  # El segundo proceso vive 5 segundos
    # Ejecutar el comando ping en el proceso2
    subprocess.run(["ping", "google.com"])

   


def cambiar_prioridad(pid, prioridad):
    for proceso in psutil.process_iter(['pid','name']):
        if proceso.info['name'] == "proceso1":
          proceso.info['pid'].nice(prioridad)

if __name__ == "__main__":
    PROCESO_PADRE_PID = os.getpid()

    proceso_principal = multiprocessing.Process(name="proceso1",target=proceso1, args=(PROCESO_PADRE_PID, ))
    proceso_secundario = multiprocessing.Process(name="proceso2",target=proceso2, args=())

    proceso_principal.start()
    proceso_secundario.start()
    listar_procesos()
    time.sleep(3)
    proceso_principal.join()
    proceso_secundario.join()

    # Listar procesos después de que todos hayan terminado

