import time
from collections import deque
from src.constants import CELL_SIZE, WINDOW_SIZE
from src.explorer import Explorer  # for shared utilities


class BFSExplorer:
    """
    A maze explorer that uses the Breadth-First Search (BFS) algorithm.
    Includes post-processing path smoothing using line-of-sight validation.
    """

    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start_pos
        self.end = maze.end_pos
        self.visited = set()
        self.parent = {}
        self.moves = []
        self.backtrack_count = 0
        self.time_taken = 0

    def solve(self):
        start_time = time.time()

        queue = deque()
        queue.append(self.start)
        self.visited.add(self.start)

        found = False
        while queue:
            current = queue.popleft()
            if current == self.end:
                found = True
                break

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = current[0] + dx, current[1] + dy
                next_pos = (nx, ny)

                if (0 <= nx < self.maze.width and
                    0 <= ny < self.maze.height and
                    self.maze.grid[ny][nx] == 0 and
                    next_pos not in self.visited):

                    queue.append(next_pos)
                    self.visited.add(next_pos)
                    self.parent[next_pos] = current

        if found:
            raw_path = self.reconstruct_path()
            self.moves = self.smooth_path(raw_path)

        self.time_taken = time.time() - start_time
        self.print_statistics()
        return self.time_taken, self.moves

    def reconstruct_path(self):
        path = []
        node = self.end
        while node != self.start:
            path.append(node)
            node = self.parent[node]
        path.append(self.start)
        return list(reversed(path))

    def can_see(self, a, b):
        """Check if there's a clear straight line from point a to b (no walls in between)."""
        x1, y1 = a
        x2, y2 = b

        if x1 != x2 and y1 != y2:
            return False  # Only allow straight horizontal/vertical lines

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if self.maze.grid[y][x1] == 1:
                    return False
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if self.maze.grid[y1][x] == 1:
                    return False
        return True

    def smooth_path(self, path):
        """
        Reduce the path to only essential waypoints using visibility (line of sight).
        """
        if not path:
            return []

        smoothed = [path[0]]
        i = 0

        while i < len(path) - 1:
            j = len(path) - 1
            while j > i:
                if self.can_see(path[i], path[j]):
                    smoothed.append(path[j])
                    i = j
                    break
                j -= 1

        return smoothed

    def print_statistics(self):
        print("\n=== Optimized BFS Maze Stats (With Path Smoothing) ===")
        print(f"Total time taken: {self.time_taken:.2f} seconds")
        print(f"Total moves made: {len(self.moves)}")
        print("Backtracking: Not applicable (BFS doesn't backtrack)")
        print("==================================\n")
