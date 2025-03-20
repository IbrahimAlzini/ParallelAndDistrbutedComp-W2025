import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from src.square import square


def sequential_loop(numbers):
    start = time.time()
    for num in numbers:
        square(num)
    end = time.time()
    return end - start


def multiprocess_per_number(numbers):
    start = time.time()
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    return end - start


def pool_map(numbers):
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(square, numbers)
    end = time.time()
    return end - start


def pool_map_async(numbers):
    start = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map_async(square, numbers)  
        results = result.get()
    end = time.time()
    return end - start


def pool_apply_async(numbers):
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = [pool.apply_async(square, (num,)) for num in numbers]
        for res in results:
            res.get()
    end = time.time()
    return end - start


def process_pool_executor(numbers):
    start = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(square, numbers)
    end = time.time()
    return end - start


def run_square_tests(n):
    numbers = list(range(n))
    print(f"\nTesting with n = {n}")

    # Sequential Loop
    seq_time = sequential_loop(numbers)
    print(f"Sequential Loop: {seq_time:.4f} seconds")

    # Multiprocess per number with try-except since an error will happen due to the high number of processes 
    try:
        mp_time = multiprocess_per_number(numbers)
        print(f"Multiprocess per number: {mp_time:.4f} seconds")
    except Exception as e:
        print(f"Error occurred in multiprocess_per_number: {e}")

    # Pool map
    pool_map_time = pool_map(numbers)
    print(f"Pool.map(): {pool_map_time:.4f} seconds")

    # Pool map_async
    pool_map_async_time = pool_map_async(numbers)
    print(f"Pool.map_async(): {pool_map_async_time:.4f} seconds")

    # Pool apply_async
    pool_apply_async_time = pool_apply_async(numbers)
    print(f"Pool.apply_async(): {pool_apply_async_time:.4f} seconds")

    # ProcessPoolExecutor
    pp_time = process_pool_executor(numbers)
    print(f"ProcessPoolExecutor: {pp_time:.4f} seconds")
