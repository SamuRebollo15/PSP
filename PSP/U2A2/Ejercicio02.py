
import threading
import random
import statistics


vector = [random.randint(1, 100) for _ in range(100)]


def calcular_promedio():
    promedio = statistics.mean(vector)
    print(f"El promedio del vector es: {promedio}")


def encontrar_max_y_min():
    maximo = max(vector)
    minimo = min(vector)
    print(f"El máximo valor del vector es: {maximo}")
    print(f"El mínimo valor del vector es: {minimo}")


def calcular_desviacion_estandar():
    desviacion_estandar = statistics.stdev(vector)
    print(f"La desviación estándar del vector es: {desviacion_estandar}")

if __name__ == "__main__":
   
    hilos = [
        threading.Thread(target=calcular_promedio),
        threading.Thread(target=encontrar_max_y_min),
        threading.Thread(target=calcular_desviacion_estandar)
    ]


    for hilo in hilos:
        hilo.start()


    for hilo in hilos:
        hilo.join()

    print("Todos los hilos han terminado.")
