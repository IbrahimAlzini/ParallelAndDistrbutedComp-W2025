from src.square_computation import run_square_tests
from src.connection_pool import run_connection_pool_test

def main():
    print("Running Square Computation Tests...")
    run_square_tests(10**6)
    run_square_tests(10**7)

    print("\nRunning Connection Pool Test...")
    run_connection_pool_test()

if __name__ == "__main__":
    main()