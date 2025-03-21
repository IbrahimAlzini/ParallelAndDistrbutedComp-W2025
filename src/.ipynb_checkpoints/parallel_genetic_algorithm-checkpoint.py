from mpi4py import MPI
import numpy as np
import pandas as pd
from src.genetic_algorithms_functions import (
    calculate_fitness,
    select_in_tournament,
    order_crossover,
    mutate,
    generate_unique_population,
)


def split_population(population, size):
    """Splits the population across processes ensuring balanced distribution."""
    chunk_sizes = [len(population) // size] * size
    for i in range(len(population) % size):
        chunk_sizes[i] += 1
    chunks = []
    start = 0
    for chunk_size in chunk_sizes:
        end = start + chunk_size
        chunks.append(population[start:end])
        start = end
    return chunks


def run_parallel_genetic_algorithm():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        print(f"[DEBUG] MPI started with {size} processes.")

    # Load and broadcast distance matrix
    if rank == 0:
        distance_matrix = pd.read_csv('data/city_distances.csv').to_numpy()
        print("[DEBUG] Process 0: Loaded distance matrix.")
    else:
        distance_matrix = None

    distance_matrix = comm.bcast(distance_matrix, root=0)
    comm.Barrier()  # Ensure all processes receive the matrix before proceeding

    # GA parameters
    num_nodes = distance_matrix.shape[0]
    population_size = 10000
    mutation_rate = 0.1
    num_generations = 200
    stagnation_limit = 5
    best_fitness = float('inf')
    stagnation_counter = 0

    # Generate initial population
    if rank == 0:
        population = generate_unique_population(population_size, num_nodes)
        print("[DEBUG] Process 0: Generated initial population.")
        chunks = split_population(population, size)
    else:
        chunks = None

    # Distribute population among processes
    local_pop = comm.scatter(chunks, root=0)
    comm.Barrier()

    for generation in range(num_generations):
        # Local fitness evaluation
        local_fitness = np.array([calculate_fitness(ind, distance_matrix) for ind in local_pop])

        # Gather fitness values from all processes
        all_fitness = comm.gather(local_fitness, root=0)

        if rank == 0:
            # Flatten fitness array from all processes
            fitness_values = np.concatenate(all_fitness)
            population = [ind for chunk in chunks for ind in chunk]

            current_best = np.min(fitness_values)
            if current_best < best_fitness:
                best_fitness = current_best
                stagnation_counter = 0
            else:
                stagnation_counter += 1

            if stagnation_counter >= stagnation_limit:
                print(f"[DEBUG] Process 0: Regenerating population at generation {generation} due to stagnation")
                best_individual = population[np.argmin(fitness_values)]
                population = generate_unique_population(population_size - 1, num_nodes)
                population.append(best_individual)
                stagnation_counter = 0

            # Selection, Crossover, and Mutation
            num_selected = len(population) // 2  # Ensuring valid selection size
            selected = select_in_tournament(population, fitness_values, number_tournaments=num_selected, tournament_size=3)
            offspring = []
            for i in range(0, len(selected), 2):
                parent1 = selected[i]
                parent2 = selected[(i + 1) % len(selected)]
                child = [0] + order_crossover(parent1[1:], parent2[1:])
                offspring.append(mutate(child, mutation_rate))

            # Replace individuals
            sorted_indices = np.argsort(fitness_values)[::-1][:len(offspring)]
            for i, idx in enumerate(sorted_indices):
                population[idx] = offspring[i]

            # Ensure unique population
            unique_population = set(tuple(ind) for ind in population)
            while len(unique_population) < population_size:
                individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
                unique_population.add(tuple(individual))
            population = [list(ind) for ind in unique_population]
            chunks = split_population(population, size)

            print(f"Generation {generation}: Best Fitness = {current_best}")

        # Broadcast updated population to all processes
        chunks = comm.bcast(chunks, root=0)
        local_pop = comm.scatter(chunks, root=0)
        comm.Barrier()

    # Final result
    if rank == 0:
        final_fitness = np.array([calculate_fitness(route, distance_matrix) for route in population])
        best_idx = np.argmin(final_fitness)
        best_route = list(map(int, population[best_idx])) 
        print("Best Route:", best_route)
        print("Total Distance:", final_fitness[best_idx])
