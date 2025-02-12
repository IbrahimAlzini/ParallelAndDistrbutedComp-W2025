from src.threads import threading_main
from src.sequential import run_seq
from src.processes import run_processes

def run_pa():
# Given execution times from running the main script
    time_sequential = run_seq() # Time taken for sequential execution
    time_threads = threading_main()  # Time taken for multi-threading execution
    time_processes = run_processes() # Time taken for multiprocessing execution

    # Computing Speedup
    speedup_threads = time_sequential / time_threads
    speedup_processes = time_sequential / time_processes
    
    # Computing Efficiency
    num_threads = 4  # 4 threads were used
    num_processes = 2  # 2 processes were used
    
    efficiency_threads = speedup_threads / num_threads
    efficiency_processes = speedup_processes / num_processes
    
    # Amdahl's Law Speedup Calculation
    # Assuming 95% of the program is parallelizable
    p = 0.95
    speedup_amdahl_threads = 1 / ((1 - p) + (p / num_threads))
    speedup_amdahl_processes = 1 / ((1 - p) + (p / num_processes))
    
    # Gustafson’s Law Speedup Calculation
    speedup_gustafson_threads = num_threads - (1 - p) * (num_threads)
    speedup_gustafson_processes = num_processes - (1 - p) * (num_processes)
    
    # Printing results
    print("Speedup (Threads):", speedup_threads)
    print("Speedup (Processes):", speedup_processes)
    
    print("Efficiency (Threads):", efficiency_threads)
    print("Efficiency (Processes):", efficiency_processes)
    
    print("Amdahl's Law Speedup (Threads):", speedup_amdahl_threads)
    print("Amdahl's Law Speedup (Processes):", speedup_amdahl_processes)
    
    print("Gustafson's Law Speedup (Threads):", speedup_gustafson_threads)
    print("Gustafson's Law Speedup (Processes):", speedup_gustafson_processes)
