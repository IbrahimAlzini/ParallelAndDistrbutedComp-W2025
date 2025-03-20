import multiprocessing
import time
import random
import os

class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.semaphore = multiprocessing.Semaphore(max_connections)

    def get_connection(self):
        self.semaphore.acquire()
        print(f"Process {os.getpid()} acquired a connection at {time.strftime('%H:%M:%S')}")

    def release_connection(self):
        self.semaphore.release()
        print(f"Process {os.getpid()} released a connection at {time.strftime('%H:%M:%S')}")

def access_database(pool):
    print(f"Process {os.getpid()} is waiting for a connection at {time.strftime('%H:%M:%S')}")
    pool.get_connection()
    time.sleep(random.uniform(0.5, 2.0))
    pool.release_connection()

def run_connection_pool_test():
    pool = ConnectionPool(3)
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=access_database, args=(pool,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("All processes completed.")