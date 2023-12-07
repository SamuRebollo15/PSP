import threading
import queue
import time
q=queue.Queue()

class Productor(threading.Thread):

        def __init__(self,q):
                threading.Thread.__init__(self)
                self.q=q
        def run(self):
                while True:
                        self.q.put(1)
                        self.q.put(2)
                        time.sleep(2)
                        print("contenido de la cola"+str(list(q.queue)))
class Consumidor (threading.Thread):
        
        def __init__(self,q):
                threading.Thread.__init__(self)
                self.q=q
        def run(self):
                while True:
                        time.sleep(1)
                        print(self.q.get())



p=Productor(q)
c=Consumidor(q)

p.start()
c.start()
        