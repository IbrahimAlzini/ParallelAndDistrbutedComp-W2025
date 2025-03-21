# # For Sequential genetic_algorithm_trial  
# import time 
# from src.genetic_algorithm_trial import run_genetic_algorithm

# if __name__ == "__main__":
#     print("Starting sequential  Genetic Algorithm Execution...")
#     start_time = time.time()
#     run_genetic_algorithm()
#     end_time = time.time()
#     sequential_time = end_time - start_time
#     print(f"Sequential execution Time: {sequential_time} seconds")
#     print("Genetic sequential Algorithm Execution Completed.")

import time
from src.parallel_genetic_algorithm import run_parallel_genetic_algorithm

if __name__ == "__main__":
    print("Starting Parallel Genetic Algorithm Execution...")
    start_time = time.time()
    run_parallel_genetic_algorithm()
    end_time = time.time()
    print(f"Parallel execution time: {end_time - start_time} seconds")
