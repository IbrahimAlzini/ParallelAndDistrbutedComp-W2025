from threading import Thread
from queue import Queue
import time
import random

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Producer notify: item N°{item} appended to queue by {self.name}')
            time.sleep(1)
        # Signal the consumers to stop
        for _ in range(3):  # Assuming there are 3 consumers
            self.queue.put(None)

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):  # Fixed method name to 'run'
        while True:
            item = self.queue.get()
            if item is None:
                # Signal to other consumers that production is done
                self.queue.put(None)
                break
            print(f'Consumer notify: {item} popped from queue by {self.name}')
            self.queue.task_done()
def run_queue():
    # Create a shared queue
    queue = Queue()
    
    # Create producer and consumer threads
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    
    # Start all threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
    print("All tasks done.")
