from src.sequential import run_seq
from src.threads import run_threads
from src.processes import run_processes

def run_performance_analysis():
    N = 10000000
    num_threads = 4
    num_processes = 4
    
    sum_seq, time_seq = run_seq(N)
    sum_threads, time_threads = run_threads(N, num_threads)
    sum_processes, time_processes = run_processes(N, num_processes)
    
    speedup_threads = time_seq / time_threads
    speedup_processes = time_seq / time_processes
    
    efficiency_threads = speedup_threads / num_threads
    efficiency_processes = speedup_processes / num_processes
    
    p = 0.95  # Assuming 95% of program is parallelizable
    speedup_amdahl_threads = 1 / ((1 - p) + (p / num_threads))
    speedup_amdahl_processes = 1 / ((1 - p) + (p / num_processes))
    
    speedup_gustafson_threads = num_threads - (1 - p) * num_threads
    speedup_gustafson_processes = num_processes - (1 - p) * num_processes
    
    print("Performance Analysis:")
    print(f"Speedup (Threads): {speedup_threads}")
    print(f"Speedup (Processes): {speedup_processes}")
    print(f"Efficiency (Threads): {efficiency_threads}")
    print(f"Efficiency (Processes): {efficiency_processes}")
    print(f"Amdahl's Law Speedup (Threads): {speedup_amdahl_threads}")
    print(f"Amdahl's Law Speedup (Processes): {speedup_amdahl_processes}")
    print(f"Gustafson's Law Speedup (Threads): {speedup_gustafson_threads}")
    print(f"Gustafson's Law Speedup (Processes): {speedup_gustafson_processes}")