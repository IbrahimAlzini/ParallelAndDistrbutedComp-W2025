import multiprocessing
import time
from src.joinRandomLetters import join_random_letters
from src.addRandomNums import add_random_numbers

# Create processes for both functions
def run_processes(num_letters = 10000000):
    total_start_time = time.time()
    process_letters = multiprocessing.Process(target=join_random_letters, args = (0,num_letters,))
    process_numbers = multiprocessing.Process(target=add_random_numbers, args = (0,num_letters,))
    # Start the processes
    process_letters.start()
    process_numbers.start()
    # Wait for all processes to complete
    process_letters.join()
    process_numbers.join()
    total_end_time = time.time()
    print(f"Total time taken for processes: {total_end_time - total_start_time} seconds")
    return total_end_time - total_start_time
