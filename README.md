# **Temperature Monitoring System**

## **1. Introduction**
This project is a **multi-threaded temperature monitoring system** that simulates readings from multiple sensors, processes the data to compute average temperatures, and displays the results in real-time without flickering. The system utilizes **Python’s threading module** to handle concurrent execution while ensuring proper synchronization between different components.

## **2. Objectives**
- Simulate temperature readings from multiple sensors.
- Process readings and calculate real-time average temperatures.
- Display the latest and average temperatures **without erasing the console**.
- Use **thread synchronization** to ensure smooth execution.

## **3. Technologies & Libraries Used**
- **Python 3.x**
- **Threading Module** (for concurrent execution)
- **Queue Module** (for thread-safe data transfer)
- **Locks & Condition Variables** (for synchronization)


## **5. Implementation Details**
### **A. Sensor Simulation (`sensor.py`)**
- **Simulates random temperature readings** (between 15°C and 40°C).
- **Updates the latest temperature every second** in a shared dictionary (`latest_temperatures`).
- **Uses `RLock` to prevent race conditions.**

### **B. Data Processing (`processor.py`)**
- **Processes temperature readings from a queue.**
- **Calculates average temperatures every 5 seconds**.
- **Uses `Condition` to notify the display thread** when new averages are available.

### **C. Display System (`display.py`)**
- **`initialize_display()` prints the initial layout** with placeholders (`--°C`).
- **`update_display()` updates latest temperatures every second**, and **updates averages every 5 seconds without flickering**.
- **Uses `Condition.wait()` to wait for new average updates instead of blindly refreshing.**

### **D. Main Program (`main.py`)**
- **Initializes all sensors, processor, and display threads**.
- **Ensures proper execution order** so that data flows smoothly.

## **6. Synchronization Mechanisms**
| **Task**                       | **Synchronization Mechanism**   | **Purpose** |
|--------------------------------|--------------------------------|-------------|
| Sensor data updates            | `RLock`                        | Prevent race conditions when updating latest temperatures. |
| Queue-based data transfer      | `Queue`                        | Ensure thread-safe communication between sensors and processors. |
| Average calculation updates    | `RLock` + `Condition`          | Prevent inconsistent data and notify the display thread when updates are available. |
| Display synchronization        | `Condition.wait()`             | Ensures averages update only when new data is processed (avoids unnecessary refreshing). |

## **7. Answers to Lab Questions**
### **1) Which synchronization metric did you use for each of the tasks?**
To ensure thread safety and proper synchronization between sensor readings, data processing, and display updates, we used the following synchronization mechanisms:

#### **A. `RLock` (Reentrant Lock) for Safe Data Access**
- **Used in:** `sensor.py`, `processor.py`, and `display.py`
- **Purpose:** Prevents race conditions when multiple threads access shared data (`latest_temperatures` and `temperature_averages`).
- **Why?** `RLock` allows the same thread to acquire the lock multiple times, ensuring smooth operation when multiple functions modify shared variables.

#### **B. `Condition` for Coordinated Execution**
- **Used in:** `processor.py` and `display.py`
- **Purpose:** Ensures that the display only updates average temperatures when new data is available.
- **Why?** `Condition.notify_all()` signals the display thread when new averages are calculated, preventing unnecessary updates and reducing CPU usage.

#### **C. `Queue` for Safe Data Transfer**
- **Used in:** `processor.py`
- **Purpose:** Collects temperature readings from multiple sensors before processing.
- **Why?** `Queue` ensures that readings are processed in a **thread-safe** manner without data loss.

#### **D. Thread Management with `daemon=True`**
- **Used in:** `main.py`
- **Purpose:** Ensures that threads automatically stop when the main program terminates.
- **Why?** Background threads for sensors, processing, and display updates do not block program exit.

### **2) Why did the professor not ask you to compute metrics?**
most likely because this lab focuses on **parallel execution, synchronization, and real-time data handling**, rather than measuring computational performance. 

.





