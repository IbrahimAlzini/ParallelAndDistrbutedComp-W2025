from queue import Queue
import threading
import time

# Create a Queue instance
data_queue = Queue()

# Producer thread function
def producer():
    for i in range(5):
        data_queue.put(i)
        print(f"Produced {i}")
        time.sleep(1)

# Consumer thread function
def consumer():
    while True:
        item = data_queue.get()
        print(f"Consumed {item}")
        data_queue.task_done()

def run_queues():
    # Set up producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer, daemon=True)
    
    # Start threads
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for the producer to finish
    producer_thread.join()
    
    # Wait for all items to be consumed
    data_queue.join()
    
    print("Processing complete")
