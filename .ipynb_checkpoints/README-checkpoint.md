# Parallel and Distributed Computing - Square Computation & Process Synchronization

## Overview
This project explores **Python multiprocessing** to optimize computational tasks and **process synchronization** using semaphores. The primary focus is on measuring performance across different multiprocessing techniques.

---

## Project Structure
.
├── main.py
├── __pycache__
│   └── tasks.cpython-312.pyc
├── README.md
├── requirements.txt
├── src
│   ├── connection_pool.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── connection_pool.cpython-312.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── square_computation.cpython-312.pyc
│   │   ├── square.cpython-311.pyc
│   │   └── square.cpython-312.pyc
│   ├── square_computation.py
│   └── square.py
└── tests
    └── __init__.py

5 directories, 15 files


---

## **Setup & Installation**
### **Prerequisites**
- Python 3.x
- `multiprocessing` (built-in)
- `concurrent.futures` (built-in)

### **Clone Repository**
```sh
git clone https://github.com/IbrahimAlzini/ParallelAndDistrbutedComp-W2025.git
cd ParallelAndDistrbutedComp-W2025

### **Run the program**
python main.py

## **Square Computation **
The square_computation.py file implements the following functionality:

Sequential Loop: Computes squares using a simple for loop.

Multiprocessing per Number: Creates a separate process for each number.

Multiprocessing Pool: Uses multiprocessing.Pool with map() and apply_async().

ProcessPoolExecutor: Uses concurrent.futures.ProcessPoolExecutor.

### **main.py output**
(parallel) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ python main.py 
Running Square Computation Tests...

Testing with n = 1000000
Sequential Loop: 0.0488 seconds
Error occurred in multiprocess_per_number: [Errno 24] Too many open files
Pool.map(): 0.1396 seconds
Pool.map_async(): 0.1236 seconds
Pool.apply_async(): 56.3712 seconds
ProcessPoolExecutor: 85.0380 seconds

Testing with n = 10000000
Sequential Loop: 0.4861 seconds
Error occurred in multiprocess_per_number: [Errno 24] Too many open files
Pool.map(): 1.5404 seconds
Pool.map_async(): 1.2897 seconds
Pool.apply_async(): 548.7623 seconds
Killed

### Conclusions :
when running the program with a list of 10^6 numbers :
 Sequential Loop was the fastest (0.0488 seconds) followed by Pool.map_async() and Pool.map().
 multiprocess_per_number did not work due to the high number of processes generated which exceeded the limit.
 Pool.apply_async() performed badly due to too many independent calls, which caused high overhead.
 ProcessPoolExecutor was the slowest (85.0380 seconds) due to additional scheduling overhead.

when running the program with a list of 10^7 numbers :
 apply_async() creates 1 process per number, so for n = 10,000,000, causing consuming enormous memory. 
 The OS detects high memory usage and terminates the process to prevent system crashes.

we also note that async execution is faster than normal map and apply

## **Connection pool (Semaphore)**
This part simulates a database connection pool where multiple processes compete for limited resources.

### **main.py output when commenting out the Square Computation Tests**
(parallel) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ python main.py 

Running Connection Pool Test...
Process 240970 is waiting for a connection at 16:34:09
Process 240970 acquired a connection at 16:34:09
Process 240971 is waiting for a connection at 16:34:09
Process 240971 acquired a connection at 16:34:09
Process 240972 is waiting for a connection at 16:34:09
Process 240972 acquired a connection at 16:34:09
Process 240973 is waiting for a connection at 16:34:09
Process 240974 is waiting for a connection at 16:34:09
Process 240975 is waiting for a connection at 16:34:09
Process 240976 is waiting for a connection at 16:34:09
Process 240977 is waiting for a connection at 16:34:09
Process 240978 is waiting for a connection at 16:34:09
Process 240979 is waiting for a connection at 16:34:09
Process 240972 released a connection at 16:34:09
Process 240973 acquired a connection at 16:34:09
Process 240971 released a connection at 16:34:10
Process 240974 acquired a connection at 16:34:10
Process 240970 released a connection at 16:34:10
Process 240975 acquired a connection at 16:34:10
Process 240975 released a connection at 16:34:11
Process 240976 acquired a connection at 16:34:11
Process 240974 released a connection at 16:34:11
Process 240977 acquired a connection at 16:34:11
Process 240973 released a connection at 16:34:11
Process 240978 acquired a connection at 16:34:11
Process 240977 released a connection at 16:34:12
Process 240979 acquired a connection at 16:34:12
Process 240976 released a connection at 16:34:12
Process 240978 released a connection at 16:34:13
Process 240979 released a connection at 16:34:13
All processes completed.

### Answering questions :
 1. What happens if more processes try to access the pool than there are available connections? 
  They wait. Semaphores Ensure only a fixed number of processes access the resource concurrently.
  
 2. How does the semaphore prevent race conditions and ensure safe access to the connections? 
  They are prevented by controlling access via semaphores, ensuring safe resource utilization.
  
# Contributors
Ibrahim Alzini


