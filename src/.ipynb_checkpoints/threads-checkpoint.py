from src.joinRandomLetters import join_random_letters
from src.addRandomNums import add_random_numbers
import threading
import time

def threading_main(num_letters = 10000000):
    total_start_time = time.time()
    start1= 0
    end1 = num_letters // 2 
    start2 = num_letters//2 
    end2 = num_letters
    # Create threads for both functions
    thread_letters_1 = threading.Thread(target=join_random_letters, args = (start1,end1))
    thread_letters_2 = threading.Thread(target=join_random_letters, args = (start2,end2))
    thread_numbers_1 = threading.Thread(target=add_random_numbers, args = (start1,end1))
    thread_numbers_2 = threading.Thread(target=add_random_numbers, args = (start2,end2))
    # Start the threads
    thread_letters_1.start()
    thread_letters_2.start()
    thread_numbers_1.start()
    thread_numbers_2.start()
    # Wait for all threads to complete
    thread_letters_1.join()
    thread_letters_2.join()
    thread_numbers_1.join()
    thread_numbers_2.join()
    total_end_time = time.time()
    print(f"Total time taken for threads: {total_end_time - total_start_time} seconds")
    return total_end_time - total_start_time
