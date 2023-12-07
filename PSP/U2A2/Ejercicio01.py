
import threading
import random
import time

def tarea_hilo(id_hilo, numero_escrituras):
    for _ in range(numero_escrituras):
  
        time.sleep(random.uniform(0.1, 0.3))
        print(f"Soy el hilo {id_hilo}")

def crear_pool_de_hilos(tamano_pool):
    hilos = []
    for i in range(1, tamano_pool + 1):
        
        numero_escrituras = random.randint(5, 15)
        hilo = threading.Thread(target=tarea_hilo, args=(i, numero_escrituras))
        hilos.append(hilo)
    return hilos

if __name__ == "__main__":
    tamano_pool = 10
    pool_de_hilos = crear_pool_de_hilos(tamano_pool)

    for hilo in pool_de_hilos:
        hilo.start()

    for hilo in pool_de_hilos:
        hilo.join()

    print("Todos los hilos han terminado.")
