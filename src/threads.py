from src.calculate_sum import calculate_sum
import threading
import time

def threaded_sum(start, end, result, index):
    result[index] = calculate_sum(start, end)

def run_threads(N=10000000, num_threads=4):
    total_start_time = time.time()
    step = N // num_threads
    threads = []
    results = [0] * num_threads
    
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i != num_threads - 1 else N
        thread = threading.Thread(target=threaded_sum, args=(start, end, results, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    total_sum = sum(results)
    total_end_time = time.time()
    execution_time = total_end_time - total_start_time
    print(f"Threaded Sum: {total_sum}, Time: {execution_time} seconds")
    return total_sum, execution_time
