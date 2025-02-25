import time
import threading
import queue
from src.sensor import latest_temperatures, lock

temperature_averages = {}  # Shared dictionary for averages
temp_queue = queue.Queue()  # Thread-safe queue
condition = threading.Condition(lock)  # Condition variable for synchronization

def process_temperatures():
    """Calculates average temperature and signals display thread when updated."""
    global temperature_averages
    sensor_data = {}

    while True:
        if not temp_queue.empty():
            sensor_id, temp = temp_queue.get()
            with lock:
                if sensor_id not in sensor_data:
                    sensor_data[sensor_id] = []
                sensor_data[sensor_id].append(temp)

                # Keep last 5 readings for average calculation
                if len(sensor_data[sensor_id]) > 5:
                    sensor_data[sensor_id].pop(0)
                
                temperature_averages[sensor_id] = sum(sensor_data[sensor_id]) / len(sensor_data[sensor_id])

                # Notify the display thread that new averages are available
                with condition:
                    condition.notify_all()
        
        time.sleep(1)  # Process readings continuously
