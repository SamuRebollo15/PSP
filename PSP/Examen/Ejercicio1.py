import random
import time
from queue import Queue
from threading import Thread

def producer(queue, pt):
    while True:
        number = random.randint(101, 499)
        queue.put(number)
        print(f"Productor produce: {number}")
        time.sleep(pt)

def consumer(queue, ct, x):
    while True:
        numbers = []
        for _ in range(x):
            numbers.append(queue.get())
        result = 1
        for num in numbers:
            result *= num
        print(f"Consumidor: {numbers}, Resultado: {result}")
        time.sleep(ct)

if __name__ == "__main__":
    queue = Queue()

    # Test case 1:1 with PT=1, CT=4, and X=3
    pt = 1
    ct = 4
    x = 3
    producer_thread = Thread(target=producer, args=(queue, pt))
    consumer_thread = Thread(target=consumer, args=(queue, ct, x))
    producer_thread.start()
    consumer_thread.start()

    # Test case 4:2 with PT=2, CT=2, and X=2
    pt = 2
    ct = 2
    x = 2
    time.sleep(5)  
    producer_thread = Thread(target=producer, args=(queue, pt))
    consumer_thread = Thread(target=consumer, args=(queue, ct, x))
    producer_thread.start()
    consumer_thread.start()

    # Test case 2:6 with PT=1, CT=10, and X=4
    pt = 1
    ct = 10
    x = 4
    time.sleep(5)  
    producer_thread = Thread(target=producer, args=(queue, pt))
    consumer_thread = Thread(target=consumer, args=(queue, ct, x))
    producer_thread.start()
    consumer_thread.start()
