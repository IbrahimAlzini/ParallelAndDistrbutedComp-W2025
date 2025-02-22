# from tests.semaphore import run_semaphore
# run_semaphore()

# from tests.conditions import run_conditions
# run_conditions()

# from tests.event import run_event
# run_event()

# from tests.barrier import run_barrier
# run_barrier()

# from tests.queues import run_queues
# run_queues()

# from tests.queue import run_queue
# run_queue()

from src.performance_analysis import run_performance_analysis
from src.part2 import run_part2

if __name__ == "__main__":
    print("Part 1:")
    run_performance_analysis()
    print("**************************************")
    print("Part 2:")
    run_part2()
