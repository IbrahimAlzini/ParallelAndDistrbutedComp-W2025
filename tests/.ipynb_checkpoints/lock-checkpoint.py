import threading

# Create a lock object
lock = threading.Lock()

# A shared resource or variable
balance = 0

# Function that modifies the shared resource
def update_balance(amount):
    global balance
    # Acquire the lock before entering the critical section
    lock.acquire()
    try:
        # Critical section where the shared resource is modified
        temp_balance = balance
        temp_balance += amount
        balance = temp_balance
    finally:
        # Release the lock after the critical section
        lock.release()

# Fix: Added missing colon in function definition
def run_lock():
    # Threads that will update the shared resource
    t1 = threading.Thread(target=update_balance, args=(100,))
    t2 = threading.Thread(target=update_balance, args=(-50,))

    # Start the threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

    # Print the updated balance
    print(f"The updated balance is {balance}")

