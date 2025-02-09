import threading
condition = threading.Condition()
# Shared data
queue = []

# Producer thread function
def producer():
    with condition:
        print("Producer adding items to the queue")
        queue.extend(range(5))  # Produce some items
        condition.notify_all()  # Notify the consumers

# Consumer thread function
def consumer():
    with condition:
        while not queue:
            condition.wait()  # Wait for items to be produced
        item = queue.pop(0)  # Consume an item
        print(f"Consumer got item: {item}")
def run_conditions():
    # Create and start producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    consumer_thread.start()
    producer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
