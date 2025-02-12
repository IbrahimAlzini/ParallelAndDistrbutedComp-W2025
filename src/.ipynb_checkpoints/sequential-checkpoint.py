import time
from src.joinRandomLetters import join_random_letters
from src.addRandomNums import add_random_numbers

def run_seq(start_letters=0, end_letters= 10000000):
    total_start_time = time.time()
    join_random_letters(start_letters,end_letters)
    add_random_numbers(start_letters,end_letters)
    total_end_time = time.time()
    print(f"Total time taken for sequential: {total_end_time - total_start_time} seconds")
    return total_end_time - total_start_time
