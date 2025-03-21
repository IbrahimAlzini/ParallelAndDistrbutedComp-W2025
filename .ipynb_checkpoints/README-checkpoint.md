# DSAI 3202 - Assignment 1 Part 2: Navigating the City with Genetic Algorithms

## Overview

This project uses a Genetic Algorithm (GA) to optimize the delivery route for a fleet of delivery vehicles in a city. The city is represented as a graph, with nodes as delivery points and edges representing distances. Initially, the problem is solved for a **single vehicle**, aiming to visit all delivery points **exactly once** and return to the depot, while **minimizing total distance traveled**.

---

## Contents

- `city_distances.csv` – Distance matrix between 32 city nodes (100000 = no direct path).
- `genetic_algorithms_functions.py` – Core GA functions (fitness, selection, crossover, mutation).
- `genetic_algorithm_trial.py` – Main script for sequential GA execution.
- `main.py` – Entry point for running sequential and parallel GA version using MPI (just uncomment the part that you want to run).
- `city_distances_extended.csv` – Extended city with 100 nodes and 4000 edges (for scalability test).
- `parallel_genetic_algorithm.py` – Main script for parallel GA version using MPI.

---

## Genetic Algorithm Summary

### Key Concepts

- **Selection:** Tournament selection chooses the fittest individuals.
- **Crossover:** Order crossover (OX) generates valid offspring.
- **Mutation:** Swaps nodes to introduce genetic diversity.
- **Fitness:** Total distance of the route (negative for minimization). Infeasible routes are heavily penalized.

---
## Completing the functions 
There are two function to complete in `genetic_algorithms_functions.py` and they were completed as the following :
def calculate_fitness(route, distance_matrix):
    """
    calculate_fitness function: total distance traveled by the car.

    Parameters:
        - route (list): A list representing the order of nodes visited in the route.
        - distance_matrix (numpy.ndarray): A matrix of the distances between nodes.
            A 2D numpy array where the element at position [i, j] represents the distance between node i and node j.
    Returns:
        - float: The negative total distance traveled (negative because we want to minimize distance).
           Returns a large negative penalty if the route is infeasible.
    """
    total_distance = 0

    for i in range(len(route) - 1):
        node1, node2 = route[i], route[i + 1]
        distance = distance_matrix[node1][node2]

        # If the distance is infeasible (disconnected nodes)
        if distance == 100000:
            return 1e6  # Large penalty, but not always the worst

        total_distance += distance

    # Include the return trip to depot (node 0)
    last_leg = distance_matrix[route[-1]][route[0]]
    if last_leg == 100000:
        return 1e6  # Large penalty if the last leg is invalid
    total_distance += last_leg

    return -total_distance

def select_in_tournament(population, scores, number_tournaments=4, tournament_size=3):
    """
    Tournament selection for genetic algorithm.

    Parameters:
        - population (list): The current population of routes.
        - scores (np.array): The calculate_fitness scores corresponding to each individual in the population.
        - number_tournaments (int): The number of tournaments to run in the population.
        - tournament_size (int): The number of individuals to compete in the tournaments.

    Returns:
        - list: A list of selected individuals for crossover.
    """
    selected = []
    for _ in range(number_tournaments):
        indices = np.random.choice(len(population), tournament_size, replace=False)
        best_idx = indices[np.argmax(scores[indices])]
        selected.append(population[best_idx])
    return selected


---
## Explanation of `genetic_algorithm_trial.py`

The script loads the distance matrix from `city_distances.csv`and initializes parameters (population size, mutation rate, generations, etc.).
Then it generates an initial population and Iteratively evolves the population using selection, crossover, mutation.
Then it Applies stagnation control to avoid getting stuck in local minima.
Outputs the best route and its total distance.

---

## The Sequential output 

The program took 8s to run and produced a feasible path :

(parallel) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ python main.py
Starting sequential  Genetic Algorithm Execution...
Generation 0: Best calculate_fitness = -1796.0
Generation 1: Best calculate_fitness = -1796.0
Generation 2: Best calculate_fitness = -1796.0
Generation 3: Best calculate_fitness = -1796.0
Generation 4: Best calculate_fitness = -1796.0
Regenerating population at generation 5 due to stagnation
Generation 6: Best calculate_fitness = -1945.0
Generation 7: Best calculate_fitness = -1945.0
Generation 8: Best calculate_fitness = -1945.0
Generation 9: Best calculate_fitness = -1945.0
Generation 10: Best calculate_fitness = -1945.0
Regenerating population at generation 11 due to stagnation
Generation 12: Best calculate_fitness = -1945.0
Generation 13: Best calculate_fitness = -1945.0
Generation 14: Best calculate_fitness = -1945.0
Generation 15: Best calculate_fitness = -1945.0
Regenerating population at generation 16 due to stagnation
Generation 17: Best calculate_fitness = -1945.0
Generation 18: Best calculate_fitness = -1945.0
Generation 19: Best calculate_fitness = -1945.0
Generation 20: Best calculate_fitness = -1945.0
Regenerating population at generation 21 due to stagnation
Generation 22: Best calculate_fitness = -1945.0
Generation 23: Best calculate_fitness = -1945.0
Generation 24: Best calculate_fitness = -1945.0
Generation 25: Best calculate_fitness = -1945.0
Regenerating population at generation 26 due to stagnation
Generation 27: Best calculate_fitness = -1945.0
Generation 28: Best calculate_fitness = -1945.0
Generation 29: Best calculate_fitness = -1945.0
Generation 30: Best calculate_fitness = -1945.0
Regenerating population at generation 31 due to stagnation
Generation 32: Best calculate_fitness = -1945.0
Generation 33: Best calculate_fitness = -1945.0
Generation 34: Best calculate_fitness = -1945.0
Generation 35: Best calculate_fitness = -1945.0
Regenerating population at generation 36 due to stagnation
Generation 37: Best calculate_fitness = -1963.0
Generation 38: Best calculate_fitness = -1963.0
Generation 39: Best calculate_fitness = -1963.0
Generation 40: Best calculate_fitness = -1963.0
Generation 41: Best calculate_fitness = -1963.0
Regenerating population at generation 42 due to stagnation
Generation 43: Best calculate_fitness = -1963.0
Generation 44: Best calculate_fitness = -1963.0
Generation 45: Best calculate_fitness = -1963.0
Generation 46: Best calculate_fitness = -1963.0
Regenerating population at generation 47 due to stagnation
Generation 48: Best calculate_fitness = -1963.0
Generation 49: Best calculate_fitness = -1963.0
Generation 50: Best calculate_fitness = -1963.0
Generation 51: Best calculate_fitness = -1963.0
Regenerating population at generation 52 due to stagnation
Generation 53: Best calculate_fitness = -1963.0
Generation 54: Best calculate_fitness = -1963.0
Generation 55: Best calculate_fitness = -1963.0
Generation 56: Best calculate_fitness = -1963.0
Regenerating population at generation 57 due to stagnation
Generation 58: Best calculate_fitness = -1976.0
Generation 59: Best calculate_fitness = -1976.0
Generation 60: Best calculate_fitness = -1976.0
Generation 61: Best calculate_fitness = -1976.0
Generation 62: Best calculate_fitness = -1976.0
Regenerating population at generation 63 due to stagnation
Generation 64: Best calculate_fitness = -1976.0
Generation 65: Best calculate_fitness = -1976.0
Generation 66: Best calculate_fitness = -1976.0
Generation 67: Best calculate_fitness = -1976.0
Regenerating population at generation 68 due to stagnation
Generation 69: Best calculate_fitness = -1976.0
Generation 70: Best calculate_fitness = -1976.0
Generation 71: Best calculate_fitness = -1976.0
Generation 72: Best calculate_fitness = -1976.0
Regenerating population at generation 73 due to stagnation
Generation 74: Best calculate_fitness = -1976.0
Generation 75: Best calculate_fitness = -1976.0
Generation 76: Best calculate_fitness = -1976.0
Generation 77: Best calculate_fitness = -1976.0
Regenerating population at generation 78 due to stagnation
Generation 79: Best calculate_fitness = -1976.0
Generation 80: Best calculate_fitness = -1976.0
Generation 81: Best calculate_fitness = -1976.0
Generation 82: Best calculate_fitness = -1976.0
Regenerating population at generation 83 due to stagnation
Generation 84: Best calculate_fitness = -1976.0
Generation 85: Best calculate_fitness = -1976.0
Generation 86: Best calculate_fitness = -1976.0
Generation 87: Best calculate_fitness = -1976.0
Regenerating population at generation 88 due to stagnation
Generation 89: Best calculate_fitness = -1976.0
Generation 90: Best calculate_fitness = -1976.0
Generation 91: Best calculate_fitness = -1976.0
Generation 92: Best calculate_fitness = -1976.0
Regenerating population at generation 93 due to stagnation
Generation 94: Best calculate_fitness = -2115.0
Generation 95: Best calculate_fitness = -2115.0
Generation 96: Best calculate_fitness = -2115.0
Generation 97: Best calculate_fitness = -2115.0
Generation 98: Best calculate_fitness = -2115.0
Regenerating population at generation 99 due to stagnation
Generation 100: Best calculate_fitness = -2115.0
Generation 101: Best calculate_fitness = -2115.0
Generation 102: Best calculate_fitness = -2115.0
Generation 103: Best calculate_fitness = -2115.0
Regenerating population at generation 104 due to stagnation
Generation 105: Best calculate_fitness = -2115.0
Generation 106: Best calculate_fitness = -2115.0
Generation 107: Best calculate_fitness = -2115.0
Generation 108: Best calculate_fitness = -2115.0
Regenerating population at generation 109 due to stagnation
Generation 110: Best calculate_fitness = -2115.0
Generation 111: Best calculate_fitness = -2115.0
Generation 112: Best calculate_fitness = -2115.0
Generation 113: Best calculate_fitness = -2115.0
Regenerating population at generation 114 due to stagnation
Generation 115: Best calculate_fitness = -2115.0
Generation 116: Best calculate_fitness = -2115.0
Generation 117: Best calculate_fitness = -2115.0
Generation 118: Best calculate_fitness = -2115.0
Regenerating population at generation 119 due to stagnation
Generation 120: Best calculate_fitness = -2115.0
Generation 121: Best calculate_fitness = -2115.0
Generation 122: Best calculate_fitness = -2115.0
Generation 123: Best calculate_fitness = -2115.0
Regenerating population at generation 124 due to stagnation
Generation 125: Best calculate_fitness = -2115.0
Generation 126: Best calculate_fitness = -2115.0
Generation 127: Best calculate_fitness = -2115.0
Generation 128: Best calculate_fitness = -2115.0
Regenerating population at generation 129 due to stagnation
Generation 130: Best calculate_fitness = -2115.0
Generation 131: Best calculate_fitness = -2115.0
Generation 132: Best calculate_fitness = -2115.0
Generation 133: Best calculate_fitness = -2115.0
Regenerating population at generation 134 due to stagnation
Generation 135: Best calculate_fitness = -2115.0
Generation 136: Best calculate_fitness = -2115.0
Generation 137: Best calculate_fitness = -2115.0
Generation 138: Best calculate_fitness = -2115.0
Regenerating population at generation 139 due to stagnation
Generation 140: Best calculate_fitness = -2115.0
Generation 141: Best calculate_fitness = -2115.0
Generation 142: Best calculate_fitness = -2115.0
Generation 143: Best calculate_fitness = -2115.0
Regenerating population at generation 144 due to stagnation
Generation 145: Best calculate_fitness = -2115.0
Generation 146: Best calculate_fitness = -2115.0
Generation 147: Best calculate_fitness = -2115.0
Generation 148: Best calculate_fitness = -2115.0
Regenerating population at generation 149 due to stagnation
Generation 150: Best calculate_fitness = -2115.0
Generation 151: Best calculate_fitness = -2115.0
Generation 152: Best calculate_fitness = -2115.0
Generation 153: Best calculate_fitness = -2115.0
Regenerating population at generation 154 due to stagnation
Generation 155: Best calculate_fitness = -2115.0
Generation 156: Best calculate_fitness = -2115.0
Generation 157: Best calculate_fitness = -2115.0
Generation 158: Best calculate_fitness = -2115.0
Regenerating population at generation 159 due to stagnation
Generation 160: Best calculate_fitness = -2115.0
Generation 161: Best calculate_fitness = -2115.0
Generation 162: Best calculate_fitness = -2115.0
Generation 163: Best calculate_fitness = -2115.0
Regenerating population at generation 164 due to stagnation
Generation 165: Best calculate_fitness = -2115.0
Generation 166: Best calculate_fitness = -2115.0
Generation 167: Best calculate_fitness = -2115.0
Generation 168: Best calculate_fitness = -2115.0
Regenerating population at generation 169 due to stagnation
Generation 170: Best calculate_fitness = -2115.0
Generation 171: Best calculate_fitness = -2115.0
Generation 172: Best calculate_fitness = -2115.0
Generation 173: Best calculate_fitness = -2115.0
Regenerating population at generation 174 due to stagnation
Generation 175: Best calculate_fitness = -2115.0
Generation 176: Best calculate_fitness = -2115.0
Generation 177: Best calculate_fitness = -2115.0
Generation 178: Best calculate_fitness = -2115.0
Regenerating population at generation 179 due to stagnation
Generation 180: Best calculate_fitness = -2115.0
Generation 181: Best calculate_fitness = -2115.0
Generation 182: Best calculate_fitness = -2115.0
Generation 183: Best calculate_fitness = -2115.0
Regenerating population at generation 184 due to stagnation
Generation 185: Best calculate_fitness = -2115.0
Generation 186: Best calculate_fitness = -2115.0
Generation 187: Best calculate_fitness = -2115.0
Generation 188: Best calculate_fitness = -2115.0
Regenerating population at generation 189 due to stagnation
Generation 190: Best calculate_fitness = -2115.0
Generation 191: Best calculate_fitness = -2115.0
Generation 192: Best calculate_fitness = -2115.0
Generation 193: Best calculate_fitness = -2115.0
Regenerating population at generation 194 due to stagnation
Generation 195: Best calculate_fitness = -2115.0
Generation 196: Best calculate_fitness = -2115.0
Generation 197: Best calculate_fitness = -2115.0
Generation 198: Best calculate_fitness = -2115.0
Regenerating population at generation 199 due to stagnation
Best Solution: [0, 10, 7, 31, 23, 12, 9, 2, 21, 20, 29, 26, 24, 4, 3, 5, 16, 28, 18, 27, 8, 15, 19, 1, 11, 6, 22, 30, 25, 17, 13, 14]
Total Distance:  -2115.0
Sequential execution Time: 8.646604537963867 seconds
Genetic sequential Algorithm Execution Completed.

---
## 6.  Parallelize the code  `parallel_genetic_algorithm.py`

- Fitness Evaluation was distributed since each individual's fitness is independent of others.
After distribution, the population is split among multiple processes, and each process evaluates fitness for its portion. This should remove the bottleneck of single-threaded fitness computation, leading to a significant speedup.

calculate_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])
were changed to :
local_fitness = np.array([calculate_fitness(route, distance_matrix) for route in local_pop])

- Genetic Operators (Selection, Crossover, Mutation) were parallelized since each process can evolve its subset of the population without waiting for others.
Now Selection, crossover, and mutation happen independently on each process, reducing synchronization needs.
This avoids the single-process bottleneck and lets each process evolve its portion of the population.

### performance metrics :
unfortunately, the program didn't live up to expectations and ran in 5 min instead of 8 sec when it was sequential

this makes the performance metrics as the following :
speedup = 8/300 = 0.267 
Efficiency = 0.267/6 = 0.004

### How to run :
- check if the main.py would run  `parallel_genetic_algorithm.py`
- mpirun -n 6 python main.py 

### output:
parallel) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ mpirun -n 6 python main.py
Starting Parallel Genetic Algorithm Execution...
[DEBUG] MPI started with 6 processes.
[DEBUG] Process 0: Loaded distance matrix.
[DEBUG] Process 0: Generated initial population.
Generation 0: Best Fitness = -1828.0
Generation 1: Best Fitness = -1828.0
Generation 2: Best Fitness = -1828.0
Generation 3: Best Fitness = -1828.0
Generation 4: Best Fitness = -1828.0
[DEBUG] Process 0: Regenerating population at generation 5 due to stagnation
Generation 5: Best Fitness = -1828.0
Generation 6: Best Fitness = -1828.0
Generation 7: Best Fitness = -1828.0
Generation 8: Best Fitness = -1828.0
Generation 9: Best Fitness = -1828.0
[DEBUG] Process 0: Regenerating population at generation 10 due to stagnation
Generation 10: Best Fitness = -1828.0
Generation 11: Best Fitness = -1863.0
Generation 12: Best Fitness = -1863.0
Generation 13: Best Fitness = -1863.0
Generation 14: Best Fitness = -1863.0
Generation 15: Best Fitness = -1863.0
[DEBUG] Process 0: Regenerating population at generation 16 due to stagnation
Generation 16: Best Fitness = -1863.0
Generation 17: Best Fitness = -2068.0
Generation 18: Best Fitness = -2068.0
Generation 19: Best Fitness = -2068.0
Generation 20: Best Fitness = -2068.0
Generation 21: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 22 due to stagnation
Generation 22: Best Fitness = -2068.0
Generation 23: Best Fitness = -2068.0
Generation 24: Best Fitness = -2068.0
Generation 25: Best Fitness = -2068.0
Generation 26: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 27 due to stagnation
Generation 27: Best Fitness = -2068.0
Generation 28: Best Fitness = -2068.0
Generation 29: Best Fitness = -2068.0
Generation 30: Best Fitness = -2068.0
Generation 31: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 32 due to stagnation
Generation 32: Best Fitness = -2068.0
Generation 33: Best Fitness = -2068.0
Generation 34: Best Fitness = -2068.0
Generation 35: Best Fitness = -2068.0
Generation 36: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 37 due to stagnation
Generation 37: Best Fitness = -2068.0
Generation 38: Best Fitness = -2068.0
Generation 39: Best Fitness = -2068.0
Generation 40: Best Fitness = -2068.0
Generation 41: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 42 due to stagnation
Generation 42: Best Fitness = -2068.0
Generation 43: Best Fitness = -2068.0
Generation 44: Best Fitness = -2068.0
Generation 45: Best Fitness = -2068.0
Generation 46: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 47 due to stagnation
Generation 47: Best Fitness = -2068.0
Generation 48: Best Fitness = -2068.0
Generation 49: Best Fitness = -2068.0
Generation 50: Best Fitness = -2068.0
Generation 51: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 52 due to stagnation
Generation 52: Best Fitness = -2068.0
Generation 53: Best Fitness = -2068.0
Generation 54: Best Fitness = -2068.0
Generation 55: Best Fitness = -2068.0
Generation 56: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 57 due to stagnation
Generation 57: Best Fitness = -2068.0
Generation 58: Best Fitness = -2068.0
Generation 59: Best Fitness = -2068.0
Generation 60: Best Fitness = -2068.0
Generation 61: Best Fitness = -2068.0
[DEBUG] Process 0: Regenerating population at generation 62 due to stagnation
Generation 62: Best Fitness = -2068.0
Generation 63: Best Fitness = -2068.0
Generation 64: Best Fitness = -2132.0
Generation 65: Best Fitness = -2132.0
Generation 66: Best Fitness = -2132.0
Generation 67: Best Fitness = -2132.0
Generation 68: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 69 due to stagnation
Generation 69: Best Fitness = -2132.0
Generation 70: Best Fitness = -2132.0
Generation 71: Best Fitness = -2132.0
Generation 72: Best Fitness = -2132.0
Generation 73: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 74 due to stagnation
Generation 74: Best Fitness = -2132.0
Generation 75: Best Fitness = -2132.0
Generation 76: Best Fitness = -2132.0
Generation 77: Best Fitness = -2132.0
Generation 78: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 79 due to stagnation
Generation 79: Best Fitness = -2132.0
Generation 80: Best Fitness = -2132.0
Generation 81: Best Fitness = -2132.0
Generation 82: Best Fitness = -2132.0
Generation 83: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 84 due to stagnation
Generation 84: Best Fitness = -2132.0
Generation 85: Best Fitness = -2132.0
Generation 86: Best Fitness = -2132.0
Generation 87: Best Fitness = -2132.0
Generation 88: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 89 due to stagnation
Generation 89: Best Fitness = -2132.0
Generation 90: Best Fitness = -2132.0
Generation 91: Best Fitness = -2132.0
Generation 92: Best Fitness = -2132.0
Generation 93: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 94 due to stagnation
Generation 94: Best Fitness = -2132.0
Generation 95: Best Fitness = -2132.0
Generation 96: Best Fitness = -2132.0
Generation 97: Best Fitness = -2132.0
Generation 98: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 99 due to stagnation
Generation 99: Best Fitness = -2132.0
Generation 100: Best Fitness = -2132.0
Generation 101: Best Fitness = -2132.0
Generation 102: Best Fitness = -2132.0
Generation 103: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 104 due to stagnation
Generation 104: Best Fitness = -2132.0
Generation 105: Best Fitness = -2132.0
Generation 106: Best Fitness = -2132.0
Generation 107: Best Fitness = -2132.0
Generation 108: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 109 due to stagnation
Generation 109: Best Fitness = -2132.0
Generation 110: Best Fitness = -2132.0
Generation 111: Best Fitness = -2132.0
Generation 112: Best Fitness = -2132.0
Generation 113: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 114 due to stagnation
Generation 114: Best Fitness = -2132.0
Generation 115: Best Fitness = -2132.0
Generation 116: Best Fitness = -2132.0
Generation 117: Best Fitness = -2132.0
Generation 118: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 119 due to stagnation
Generation 119: Best Fitness = -2132.0
Generation 120: Best Fitness = -2132.0
Generation 121: Best Fitness = -2132.0
Generation 122: Best Fitness = -2132.0
Generation 123: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 124 due to stagnation
Generation 124: Best Fitness = -2132.0
Generation 125: Best Fitness = -2132.0
Generation 126: Best Fitness = -2132.0
Generation 127: Best Fitness = -2132.0
Generation 128: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 129 due to stagnation
Generation 129: Best Fitness = -2132.0
Generation 130: Best Fitness = -2132.0
Generation 131: Best Fitness = -2132.0
Generation 132: Best Fitness = -2132.0
Generation 133: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 134 due to stagnation
Generation 134: Best Fitness = -2132.0
Generation 135: Best Fitness = -2132.0
Generation 136: Best Fitness = -2132.0
Generation 137: Best Fitness = -2132.0
Generation 138: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 139 due to stagnation
Generation 139: Best Fitness = -2132.0
Generation 140: Best Fitness = -2132.0
Generation 141: Best Fitness = -2132.0
Generation 142: Best Fitness = -2132.0
Generation 143: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 144 due to stagnation
Generation 144: Best Fitness = -2132.0
Generation 145: Best Fitness = -2132.0
Generation 146: Best Fitness = -2132.0
Generation 147: Best Fitness = -2132.0
Generation 148: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 149 due to stagnation
Generation 149: Best Fitness = -2132.0
Starting Parallel Genetic Algorithm Execution...
Parallel execution time: 299.9599812030792 seconds
Starting Parallel Genetic Algorithm Execution...
Parallel execution time: 299.95508909225464 seconds
Starting Parallel Genetic Algorithm Execution...
Parallel execution time: 299.90678453445435 seconds
Starting Parallel Genetic Algorithm Execution...
Parallel execution time: 299.9483759403229 seconds
Starting Parallel Genetic Algorithm Execution...
Parallel execution time: 299.9615993499756 seconds
Generation 150: Best Fitness = -2132.0
Generation 151: Best Fitness = -2132.0
Generation 152: Best Fitness = -2132.0
Generation 153: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 154 due to stagnation
Generation 154: Best Fitness = -2132.0
Generation 155: Best Fitness = -2132.0
Generation 156: Best Fitness = -2132.0
Generation 157: Best Fitness = -2132.0
Generation 158: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 159 due to stagnation
Generation 159: Best Fitness = -2132.0
Generation 160: Best Fitness = -2132.0
Generation 161: Best Fitness = -2132.0
Generation 162: Best Fitness = -2132.0
Generation 163: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 164 due to stagnation
Generation 164: Best Fitness = -2132.0
Generation 165: Best Fitness = -2132.0
Generation 166: Best Fitness = -2132.0
Generation 167: Best Fitness = -2132.0
Generation 168: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 169 due to stagnation
Generation 169: Best Fitness = -2132.0
Generation 170: Best Fitness = -2132.0
Generation 171: Best Fitness = -2132.0
Generation 172: Best Fitness = -2132.0
Generation 173: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 174 due to stagnation
Generation 174: Best Fitness = -2132.0
Generation 175: Best Fitness = -2132.0
Generation 176: Best Fitness = -2132.0
Generation 177: Best Fitness = -2132.0
Generation 178: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 179 due to stagnation
Generation 179: Best Fitness = -2132.0
Generation 180: Best Fitness = -2132.0
Generation 181: Best Fitness = -2132.0
Generation 182: Best Fitness = -2132.0
Generation 183: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 184 due to stagnation
Generation 184: Best Fitness = -2132.0
Generation 185: Best Fitness = -2132.0
Generation 186: Best Fitness = -2132.0
Generation 187: Best Fitness = -2132.0
Generation 188: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 189 due to stagnation
Generation 189: Best Fitness = -2132.0
Generation 190: Best Fitness = -2132.0
Generation 191: Best Fitness = -2132.0
Generation 192: Best Fitness = -2132.0
Generation 193: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 194 due to stagnation
Generation 194: Best Fitness = -2132.0
Generation 195: Best Fitness = -2132.0
Generation 196: Best Fitness = -2132.0
Generation 197: Best Fitness = -2132.0
Generation 198: Best Fitness = -2132.0
[DEBUG] Process 0: Regenerating population at generation 199 due to stagnation
Generation 199: Best Fitness = -2132.0
Best Route: [0, 28, 15, 23, 3, 7, 24, 21, 2, 31, 10, 27, 29, 17, 13, 8, 26, 4, 11, 12, 9, 6, 14, 5, 16, 1, 20, 25, 19, 18, 30, 22]
Total Distance: -2132.0
Parallel execution time: 300.003867149353 seconds

---

## Enhancements 

### Distribution Over Multiple Machines 
I tried sending my file to the machines in the machines.txt file but i was met with several errors because of the imported modes such as pandas and NumPy

I used the following command to run it :
mpirun -hostfile machines.txt -n 18 python main.py

---

## Large Scale Problem 

### How to Add More Cars 
To support multiple vehicles we can Partition the node set among vehicles using clustering, KMeans for example.
We could then run the GA on each vehicle's assigned cluster independently.
And apply global synchronization to optimize fleet-wide efficiency.

