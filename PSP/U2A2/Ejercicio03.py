

import random
import threading


numbers_list = []


sum_value = 0


lock = threading.Lock()


def generate_numbers():
    global sum_value
    while sum_value <= 20000:
        number = random.randint(1, 100)
        with lock:
            numbers_list.append(number) 
            sum_value += number


def replace_numbers():
    global sum_value
    while sum_value <= 20000:
        with lock:
            for i in range(len(numbers_list)):
                if numbers_list[i] % 10 == 0: 
                    numbers_list[i] = -1


def abort_threads():
    global sum_value
    while sum_value <= 20000:
        pass
    print("Suma de elementos superó 20000. Abortando hilos...")
    thread1.join()
    thread2.join()


thread1 = threading.Thread(target=generate_numbers)
thread2 = threading.Thread(target=replace_numbers)
thread3 = threading.Thread(target=abort_threads)


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Lista resultante:", numbers_list)