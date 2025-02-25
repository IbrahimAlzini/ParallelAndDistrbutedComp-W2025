import threading
import time
from src.sensor import simulate_sensor, latest_temperatures
from src.processor import process_temperatures, temp_queue
from src.display import initialize_display, update_display

def main():
    initialize_display()  # Print the initial display layout before updates start

    # Initialize and start sensor threads
    sensor_threads = []
    for i in range(3):
        thread = threading.Thread(target=simulate_sensor, args=(i,), daemon=True)
        sensor_threads.append(thread)
        thread.start()
    
    # Start data processing thread
    processing_thread = threading.Thread(target=process_temperatures, daemon=True)
    processing_thread.start()

    # Start unified display thread
    display_thread = threading.Thread(target=update_display, daemon=True)
    display_thread.start()

    # Main thread keeps running
    while True:
        with threading.RLock():
            for sensor_id, temp in latest_temperatures.items():
                temp_queue.put((sensor_id, temp))  # Send readings to processing
        time.sleep(1)  # Ensure queue gets updated every second

if __name__ == "__main__":
    main()
