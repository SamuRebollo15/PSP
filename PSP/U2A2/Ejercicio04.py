

import threading
import random

def sumar_numeros_aleatorios():
    numbers = [random.randint(1, 1000) for _ in range(100)]
    result = sum(numbers) 
    print(f"Thread {threading.current_thread().name}: {result}") 



threads = []

for i in range(10): 
    thread = threading.Thread(target=sumar_numeros_aleatorios) 
    threads.append(thread) 
    thread.start() 

for thread in threads:
    thread.join() 