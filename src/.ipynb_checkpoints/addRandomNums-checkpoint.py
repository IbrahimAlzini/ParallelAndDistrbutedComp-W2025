import random
# Function to add a thousand random numbers
def add_random_numbers(start = 0, end = 1000):
    numbers = [random.randint(1, 100) for _ in range(start, end)]
    total_sum = sum(numbers)
    return total_sum
