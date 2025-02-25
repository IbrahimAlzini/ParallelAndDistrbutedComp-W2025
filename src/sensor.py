import random
import time
import threading

latest_temperatures = {}  # Shared dictionary for latest readings
lock = threading.RLock()  # Synchronization lock

def simulate_sensor(sensor_id):
    global latest_temperatures
    while True:
        temp = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temp
        time.sleep(1)  # Update every second
