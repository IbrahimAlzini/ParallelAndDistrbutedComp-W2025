import threading
import time

# A semaphore with 2 permits
semaphore = threading.Semaphore(2)

# Shared resource
resource_pool = []

# Thread function to access the shared resource
def access_resource(thread_id):
    print(f"Thread {thread_id} is attempting to access the resource.")
    with semaphore:
        # Critical section with limited access
        print(f"Thread {thread_id} has entered the critical section.")
        resource_pool.append(thread_id)
        time.sleep(1)  # Simulate resource usage
        print(f"Thread {thread_id} is leaving the critical section.")
        resource_pool.remove(thread_id)
def run_semaphore():
    # Create and start 5 threads
    threads = []  # Store threads to join later
    for i in range(5):
        t = threading.Thread(target=access_resource, args=(i,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print("All threads have finished execution.")
