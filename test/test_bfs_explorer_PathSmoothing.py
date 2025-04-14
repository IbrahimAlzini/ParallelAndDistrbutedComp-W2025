import sys
import os
import time

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.maze import StaticMaze
from src.BFSExplorer_PathSmoothing import BFSExplorer  

def run_bfs_test():
    print("=== BFS Explorer Test (Static Maze with Path Smoothing) ===")

    # Initialize static maze
    maze = StaticMaze(0, 0)
    maze.start_pos = (11, 0)
    maze.end_pos = (13, maze.height - 1)
    maze.grid[maze.start_pos[1]][maze.start_pos[0]] = 0
    maze.grid[maze.end_pos[1]][maze.end_pos[0]] = 0

    # Run the explorer
    explorer = BFSExplorer(maze)
    time_taken, moves = explorer.solve()

    # Output summary
    print(f"\nTotal time taken : {time_taken:.4f} seconds")
    print(f"Total moves made : {len(moves)}")
    print("===========================================================\n")

if __name__ == "__main__":
    run_bfs_test()
