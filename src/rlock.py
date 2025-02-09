import threading

# Create an RLock object
rlock = threading.RLock()

# A shared resource or variable
counter = 0

# A recursive function that modifies the shared resource
def increment_counter(depth):
    global counter
    if depth > 0:
        rlock.acquire()
        try:
            counter += 1
            increment_counter(depth - 1)  # Recursive call
        finally:
            rlock.release()
    else:
        print("Reached the recursive base case.")

def run_rlock():
    # Thread that will use the recursive function
    t = threading.Thread(target=increment_counter, args=(5,))

    # Start the thread
    t.start()

    # Wait for the thread to complete
    t.join()

    # Print the updated counter
    print(f"The updated counter is {counter}")


