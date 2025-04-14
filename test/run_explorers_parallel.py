import sys
import os

# Add the root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
import multiprocessing
import time
from src.maze import create_maze
from src.explorer import Explorer

def run_explorer(index, maze_type, width, height, return_dict):
    maze = create_maze(width, height, maze_type)
    explorer = Explorer(maze, visualize=False)
    time_taken, moves = explorer.solve()

    result = {
        'explorer_id': index,
        'time_taken': time_taken,
        'num_moves': len(moves),
        'backtracks': explorer.backtrack_count
    }
    return_dict[index] = result

def main():
    num_explorers = 4 
    maze_type = "static"  # or "random"
    width, height = 30, 30  # ignored for static maze

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    processes = []

    for i in range(num_explorers):
        p = multiprocessing.Process(target=run_explorer, args=(i, maze_type, width, height, return_dict))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Print results
    print("\n--- Parallel Maze Solver Results ---")
    best = None
    for i in range(num_explorers):
        result = return_dict[i]
        print(f"Explorer {result['explorer_id']}:")
        print(f"  Time Taken     : {result['time_taken']:.2f}s")
        print(f"  Moves Made     : {result['num_moves']}")
        print(f"  Backtrack Ops  : {result['backtracks']}")
        print()

        if best is None or result['num_moves'] < best['num_moves']:
            best = result

    print("Best Explorer:")
    print(f"  Explorer {best['explorer_id']} with {best['num_moves']} moves and {best['time_taken']:.2f}s")

if __name__ == "__main__":
    main()
