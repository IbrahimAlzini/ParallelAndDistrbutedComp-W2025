from src.sequential import run_seq
from src.threads import run_threads
from src.processes import run_processes

def run_performance_analysis():
    N = 10000000
    num_threads = 6
    num_processes = 6
    np = 6
    
    sum_seq, time_seq = run_seq(N)
    sum_threads, time_threads = run_threads(N, num_threads)
    sum_processes, time_processes = run_processes(N, num_processes)
    
    speedup_threads = time_seq / time_threads
    speedup_processes = time_seq / time_processes
    
    efficiency_threads = speedup_threads / np
    efficiency_processes = speedup_processes / np
    
    p = 0.90  # Assuming 90% of program is parallelizable
    speedup_amdahl_threads = 1 / ((1 - p) + (p / np))
    speedup_amdahl_processes = 1 / ((1 - p) + (p / np))
    
    speedup_gustafson_threads = np - (1 - p) * np
    speedup_gustafson_processes = np - (1 - p) * np
    
    print("Performance Analysis:")
    print(f"Speedup (Threads): {speedup_threads}")
    print(f"Speedup (Processes): {speedup_processes}")
    print(f"Efficiency (Threads): {efficiency_threads}")
    print(f"Efficiency (Processes): {efficiency_processes}")
    print(f"Amdahl's Law Speedup (Threads): {speedup_amdahl_threads}")
    print(f"Amdahl's Law Speedup (Processes): {speedup_amdahl_processes}")
    print(f"Gustafson's Law Speedup (Threads): {speedup_gustafson_threads}")
    print(f"Gustafson's Law Speedup (Processes): {speedup_gustafson_processes}")