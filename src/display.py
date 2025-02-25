import time
import os
import threading
from src.sensor import latest_temperatures, lock
from src.processor import temperature_averages, condition

def initialize_display():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nCurrent temperatures:\n")
    print("Latest Temperatures:")
    for i in range(3):
        print(f"Sensor {i}: --°C ", end=" ")
    print("\n\nAverage Temperatures:")
    for i in range(3):
        print(f"Sensor {i} Average: --°C")

def update_display():
    last_avg_update = time.time()
    stored_averages = {0: "--", 1: "--", 2: "--"}  # Store the last computed averages

    while True:
        with lock:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console
            print("\nCurrent temperatures:\n")

            # Print latest temperatures (updated every second)
            print("Latest Temperatures:")
            for i in range(3):
                temp = latest_temperatures.get(i, "--")
                print(f"Sensor {i}: {temp}°C ", end=" ")
            print("\n")

            # Ensure average temperatures update every 5 seconds
            if time.time() - last_avg_update >= 5:
                with condition:
                    condition.wait(timeout=5)  # Wait for processing updates
                    for i in range(3):
                        avg_temp = temperature_averages.get(i, "--")
                        if isinstance(avg_temp, (int, float)):
                            stored_averages[i] = f"{avg_temp:.2f}°C"
                        else:
                            stored_averages[i] = "--°C"
                    last_avg_update = time.time()  # Reset timer

            # Always display stored averages (no flickering)
            print("\nAverage Temperatures:")
            for i in range(3):
                print(f"Sensor {i} Average: {stored_averages[i]}")

        time.sleep(1)  # Update latest temperatures every second
