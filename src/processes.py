from src.calculate_sum import calculate_sum
import multiprocessing
import time

def process_sum(start, end, queue):
    queue.put(calculate_sum(start, end))

def run_processes(N=10000000, num_processes=6):
    total_start_time = time.time()
    step = N // num_processes
    processes = []
    queue = multiprocessing.Queue()
    
    for i in range(num_processes):
        start = i * step + 1
        end = (i + 1) * step if i != num_processes - 1 else N
        process = multiprocessing.Process(target=process_sum, args=(start, end, queue))
        processes.append(process)
        process.start()
    
    results = [queue.get() for _ in processes]
    
    for process in processes:
        process.join()
    
    total_sum = sum(results)
    total_end_time = time.time()
    execution_time = total_end_time - total_start_time
    print(f"Multiprocessing Sum: {total_sum}, Time: {execution_time} seconds")
    return total_sum, execution_time
