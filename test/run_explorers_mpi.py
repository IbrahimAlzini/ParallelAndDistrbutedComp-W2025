import sys
import os

# Add the root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from mpi4py import MPI
from src.maze import create_maze
from src.explorer import Explorer

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

maze_type = "static"  # or "random"
width, height = 30, 30  # Ignored for static

def run_explorer(index):
    maze = create_maze(width, height, maze_type)
    explorer = Explorer(maze, visualize=False)
    time_taken, moves = explorer.solve()
    return {
        'explorer_id': index,
        'time_taken': time_taken,
        'num_moves': len(moves),
        'backtracks': explorer.backtrack_count
    }

if rank == 0:
    print(f"Running {size - 1} explorers using MPI...\n")
    results = []

    for i in range(1, size):
        data = comm.recv(source=i)
        results.append(data)

    print("\n--- MPI Maze Solving Results ---")
    best = None
    for result in results:
        print(f"Explorer {result['explorer_id']}:")
        print(f"  Time Taken     : {result['time_taken']:.2f}s")
        print(f"  Moves Made     : {result['num_moves']}")
        print(f"  Backtrack Ops  : {result['backtracks']}")
        print()

        if best is None or result['num_moves'] < best['num_moves']:
            best = result

    print(" Best Explorer:")
    print(f"  Explorer {best['explorer_id']} with {best['num_moves']} moves and {best['time_taken']:.2f}s")

else:
    result = run_explorer(rank)
    comm.send(result, dest=0)
