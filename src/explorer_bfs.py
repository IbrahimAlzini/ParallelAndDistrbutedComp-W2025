import time
from collections import deque
from src.constants import CELL_SIZE, WINDOW_SIZE
from src.explorer import Explorer  # for shared utilities


class BFSExplorer:
    """
    A maze explorer that uses the Breadth-First Search (BFS) algorithm.
    This algorithm guarantees the shortest path in an unweighted grid.
    """

    def __init__(self, maze):
        """
        Initialize the BFS explorer with a maze.

        Parameters:
        - maze: an instance of the Maze class, with .grid, .start_pos, .end_pos, .width, .height
        """
        self.maze = maze
        self.start = maze.start_pos
        self.end = maze.end_pos
        self.visited = set()            # Track visited positions
        self.parent = {}                # Map each cell to its predecessor for path reconstruction
        self.moves = []                 # Final list of steps (from start to end)
        self.backtrack_count = 0        # Not used in BFS but kept for compatibility
        self.time_taken = 0             # Time to solve the maze

    def solve(self):
        """
        Solve the maze using BFS. Traverses level by level until the goal is found.

        Returns:
        - self.time_taken (float): Time in seconds
        - self.moves (list): List of (x, y) steps from start to end
        """
        start_time = time.time()

        queue = deque()
        queue.append(self.start)
        self.visited.add(self.start)

        found = False

        # BFS traversal loop
        while queue:
            current = queue.popleft()

            if current == self.end:
                found = True
                break

            # Explore 4 cardinal directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = current[0] + dx, current[1] + dy
                next_pos = (nx, ny)

                # Check boundaries, walls, and avoid revisits
                if (0 <= nx < self.maze.width and
                    0 <= ny < self.maze.height and
                    self.maze.grid[ny][nx] == 0 and
                    next_pos not in self.visited):

                    queue.append(next_pos)
                    self.visited.add(next_pos)
                    self.parent[next_pos] = current  # Track path

        # If the goal was found, reconstruct the path
        if found:
            self.moves = self.reconstruct_path()

        self.time_taken = time.time() - start_time
        self.print_statistics()
        return self.time_taken, self.moves

    def reconstruct_path(self):
        """
        Reconstruct the path from end to start using the parent map.

        Returns:
        - path (list): Reversed list of steps from start to end
        """
        path = []
        node = self.end
        while node != self.start:
            path.append(node)
            node = self.parent[node]
        path.append(self.start)
        return list(reversed(path))

    def print_statistics(self):
        """
        Print BFS execution statistics.
        """
        print("\n=== Optimized BFS Maze Stats ===")
        print(f"Total time taken: {self.time_taken:.2f} seconds")
        print(f"Total moves made: {len(self.moves)}")
        print("Backtracking: Not applicable (BFS doesn't backtrack)")
        print("==================================\n")
