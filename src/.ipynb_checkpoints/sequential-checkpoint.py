from src.calculate_sum import calculate_sum
import time

def run_seq(N=10000000):
    total_start_time = time.time()
    total_sum = calculate_sum(1, N)
    total_end_time = time.time()
    execution_time = total_end_time - total_start_time
    print(f"Sequential Sum: {total_sum}, Time: {execution_time} seconds")
    return total_sum, execution_time