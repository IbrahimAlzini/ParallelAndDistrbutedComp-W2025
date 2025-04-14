# Maze Explorer Game

A simple maze exploration game built with Pygame where you can either manually navigate through a maze or watch an automated solver find its way to the exit.

## Getting Started

### 1. Connect to Your VM

1. Open **<span style="color:red">Visual Studio Code</span>**
2. Install the "Remote - SSH" extension if you haven't already
3. Connect to your VM using SSH:
   - Press `Ctrl+Shift+P` to open the command palette
   - Type "Remote-SSH: Connect to Host..."
   - Enter your VM's SSH connection details
   - Enter your credentials when prompted

4. Install required VS Code extensions:
   - Press `Ctrl+Shift+X` to open the Extensions view
   - Search for and install "Python Extension Pack"
   - Search for and install "Jupyter"
   - These extensions will provide Python language support, debugging, and Jupyter notebook functionality

### 2. Project Setup

1. Create and activate a Conda environment:
```bash
# Create a new conda environment with Python 3.12
conda create -n maze-runner python=3.12

# Activate the conda environment
conda activate maze-runner
```

2. Install Jupyter and the required dependencies:
```bash
# Install Jupyter
pip install jupyter

# Install project dependencies
pip install -r requirements.txt
```

3. Open the project in Visual Studio Code and select the interpreter:
   - Press `Ctrl+Shift+P` to open the command palette
   - Type "Python: Select Interpreter"
   - Choose the interpreter from the `maze-runner` environment

## Running the Game

### Basic Usage
Run the game with default settings (30x30 random maze):
```bash
python main.py
```

### Manual Mode (Interactive)
Use arrow keys to navigate through the maze:
```bash
# Run with default random maze
python main.py

# Run with static maze
python main.py --type static

# Run with custom maze dimensions
python main.py --width 40 --height 40
```

### Automated Mode (Explorer)
The explorer will automatically solve the maze and show statistics:

#### Without Visualization (Text-only)
```bash
# Run with default random maze
python main.py --auto

# Run with static maze
python main.py --type static --auto

# Run with custom maze dimensions
python main.py --width 40 --height 40 --auto
```

#### With Visualization (Watch the Explorer in Action)
```bash
# Run with default random maze
python main.py --auto --visualize

# Run with static maze
python main.py --type static --auto --visualize

# Run with custom maze dimensions
python main.py --width 40 --height 40 --auto --visualize
```

### Jupyter Notebook Visualization
To run the maze visualization in Jupyter Notebook:

1. Make sure you have activated your virtual environment and installed all dependencies
2. Open the project in Visual Studio Code
3. Select the correct Python interpreter:
   - Press `Ctrl+Shift+P` to open the command palette
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your created environment:
     - If using venv: Select the interpreter from `venv/bin/python` (Linux/Mac) or `venv\Scripts\python.exe` (Windows)
     - If using Conda: Select the interpreter from the `maze-runner` environment
4. Open the `maze_visualization.ipynb` notebook in VS Code
5. VS Code will automatically start a Jupyter server
6. Run all cells to see the maze visualization in action

Available arguments:
- `--type`: Choose between "random" (default) or "static" maze generation
- `--width`: Set maze width (default: 30, ignored for static mazes)
- `--height`: Set maze height (default: 30, ignored for static mazes)
- `--auto`: Enable automated maze exploration
- `--visualize`: Show real-time visualization of the automated exploration

## Maze Types

### Random Maze (Default)
- Generated using depth-first search algorithm
- Different layout each time you run the program
- Customizable dimensions
- Default type if no type is specified

### Static Maze
- Predefined maze pattern
- Fixed dimensions (50x50)
- Same layout every time
- Width and height arguments are ignored

## How to Play

### Manual Mode
1. Controls:
- Use the arrow keys to move the player (<span style="color:blue">blue circle</span>)
- Start at the <span style="color:green">green square</span>
- Reach the <span style="color:red">red square</span> to win
- Avoid the <span style="color:black">black walls</span>

### Automated Mode
- The explorer uses the right-hand rule algorithm to solve the maze
- Automatically finds the path from start to finish
- Displays detailed statistics at the end:
  - Total time taken
  - Total moves made
  - Number of backtrack operations
  - Average moves per second
- Works with both random and static mazes
- Optional real-time visualization:
  - Shows the explorer's position in <span style="color:blue">blue</span>
  - Updates at 30 frames per second
  - Pauses for 2 seconds at the end to show the final state

## Project Structure

```
maze-runner/
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── maze.py
│   ├── player.py
│   ├── game.py
│   ├── explorer.py
│   └── visualization.py
├── main.py
├── maze_visualization.ipynb
├── requirements.txt
└── README.md
```

## Code Overview

### Main Files
- `main.py`: Entry point of the game. Handles command-line arguments and initializes the game with specified parameters.
- `requirements.txt`: Lists all Python package dependencies required to run the game.

### Source Files (`src/` directory)
- `__init__.py`: Makes the src directory a Python package.
- `constants.py`: Contains all game constants like colors, screen dimensions, cell sizes, and game settings.
- `maze.py`: Implements maze generation using depth-first search algorithm and handles maze-related operations.
- `player.py`: Manages player movement, collision detection, and rendering of the player character.
- `game.py`: Core game implementation including the main game loop, event handling, and game state management.
- `explorer.py`: Implements automated maze solving using the right-hand rule algorithm and visualization.
- `visualization.py`: Contains functions for maze visualization.

## Game Features

- Randomly generated maze using depth-first search algorithm
- Predefined static maze option
- Manual and automated exploration modes
- Real-time visualization of automated exploration
- Smooth player movement
- Collision detection with walls
- Win condition when reaching the exit
- Performance metrics (time and moves) for automated solving

## Development

The project is organized into several modules:
- `constants.py`: Game constants and settings
- `maze.py`: Maze generation and management
- `player.py`: Player movement and rendering
- `game.py`: Game implementation and main loop
- `explorer.py`: Automated maze solving implementation and visualization
- `visualization.py`: Functions for maze visualization

## Getting Started with the Assignment

Before attempting the questions below, please follow these steps:

1. Open the `maze_visualization.ipynb` notebook in VS Code
2. Run all cells in the notebook to:
   - Understand how the maze is generated
   - See how the explorer works
   - Observe the visualization of the maze solving process
   - Get familiar with the statistics and metrics

This will help you better understand the system before attempting the questions.

## Student Questions

### Question 1 (10 points)
Explain how the automated maze explorer works. Your answer should include:
1. The algorithm used by the explorer
2. How it handles getting stuck in loops
3. The backtracking strategy it employs
4. The statistics it provides at the end of exploration

To answer this question:
1. Run the explorer both with and without visualization
2. Observe its behavior in different maze types
3. Analyze the statistics it provides
4. Read the source code in `explorer.py` to understand the implementation details

#### Answer: 
1. The algorithm used by the explorer:
The explorer uses the Right-Hand Rule, which always try to keep it's the right hand on the wall.
based on my understanding of the code, It Implements it as the following:
First, turn right and try to move. If that fails, try to move forward. If that fails, turn left and try to move. If all directions are blocked, perform a 180° turn and backtrack. 

2. How it handles getting stuck in loops:
The explorer handles getting stuck in loops by using the "is_stuck(self) -> bool" function which return true if the last 3 positions were the same

3. The backtracking strategy it employs:
When the explorer is stuck, it activates the backtracking mechanism to return to a decision point as the following:
find_backtrack_path() searches the move history in reverse to find the most recent position with multiple unvisited directions, then a backtrack path is generated from the current position to that fork. The explorer moves along this path until it reaches a new branching point.
Backtracking operations are counted via self.backtrack_count for reporting.

4. The statistics it provides at the end of exploration

=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 728577.32

These are calculated using:
time_taken = self.end_time - self.start_time
len(self.moves) for move count
self.backtrack_count for backtracks
Moves per second = len(self.moves) / time_taken

This data is then printed via the print_statistics() function.

This explorer guarantees a path, which includes both the static and random mazes in this project, but  it's not efficient.

### Question 2 (30 points)
Modify the main program to run multiple maze explorers simultaneously. This is because we want to find the best route out of the maze. Your solution should:
1. Allow running multiple explorers in parallel
2. Collect and compare statistics from all explorers
3. Display a summary of results showing which explorer performed best

*Hints*:
- To get 20 points, use use multiprocessing.
- To get 30 points, use MPI4Py on multiple machines.
- Use Celery and RabbitMQ to distribute the exploration tasks. You will get full marks plus a bonus.
- Implement a task queue system
- Do not visualize the exploration, just run it in parallel
- Store results for comparison

**To answer this question:** 
1. Study the current explorer implementation
2. Design a parallel execution system
3. Implement task distribution
4. Create a results comparison system

#### Answer :
To answer this question I created two files to test both multiprocessing and MPI4Py in the test folder (i didn't know how to change the main file to run them while keeping it's functionality)

- To get 20 points, use use multiprocessing:
run_explorers_parallel.py is the file created to perform multiprocessing.
how to run :
python test/run_explorers_parallel.py

output :
(maze-runner) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ python run_explorers_parallel.py
pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 922847.90
==================================


=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 706787.20
==================================


=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 664007.28
==================================


=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 909856.65
==================================


--- Parallel Maze Solver Results ---
Explorer 0:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Explorer 1:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Explorer 2:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Explorer 3:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Best Explorer:
  Explorer 0 with 1279 moves and 0.00s

conclution :
all explorers made the same number of moves and the only diffreance is the Average moves per second which was the best in explorer 0 : 922847.90

##### - To get 30 points, use MPI4Py on multiple machines: 
run_explorers_mpi.py was made to test mpi4py.

how to run :
mpirun -n 5 test/python run_explorers_mpi.py

(maze-runner) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025/test$ mpirun -n 5 python run_explorers_mpi.py
pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 489507.69
==================================

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 432308.39
==================================

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 318047.95
==================================

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 328406.17
==================================

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html
Running 4 explorers using MPI...


--- MPI Maze Solving Results ---
Explorer 1:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Explorer 2:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Explorer 3:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

Explorer 4:
  Time Taken     : 0.00s
  Moves Made     : 1279
  Backtrack Ops  : 0

 Best Explorer:
  Explorer 1 with 1279 moves and 0.00s

conclution :
all explorers made the same number of moves 

### Question 3 (10 points)
Analyze and compare the performance of different maze explorers on the static maze. Your analysis should:

1. Run multiple explorers (at least 4 ) simultaneously on the static maze
2. Collect and compare the following metrics for each explorer:
   - Total time taken to solve the maze
   - Number of moves made
   - *Optional*:
     - Number of backtrack operations

3. What do you notice regarding the performance of the explorers? Explain the results and the observations you made.

#### Answer :
using the output of the run_explorers_parallel.py file :
=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 922847.90
==================================


=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 706787.20
==================================


=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 664007.28
==================================


=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 909856.65
==================================

we can see that when we run 4 explorers simultaneously that they all used the same number of moves (1279) and the same amount of time. this is because we used the same explorer type wich will use the same sarching method. the only defferance are the Average moves per second on each explorer.

### Question 4 (20 points)
Based on your analysis from Question 3, propose and implement enhancements to the maze explorer to overcome its limitations. Your solution should:

1. Identify and explain the main limitations of the current explorer:

2. Propose specific improvements to the exploration algorithm:

3. Implement at least two of the proposed improvements:

Your answer should include:
1. A detailed explanation of the identified limitations
2. Documentation of your proposed improvements
3. The modified code with clear comments explaining the changes

#### Answer :
After analyzing the performance of the original explorer, several limitations were identified:
The right-hand rule is inherently greedy and non-optimal.
The algorithm does not avoid revisiting paths, resulting in redundant moves.

Two improvements were implemented in (src/explorer_bfs):
Marking visited cells: This avoids revisiting already explored nodes.
Switching to BFS: Breadth-First Search ensures the shortest path in unweighted grids, guaranteeing optimal move count.

These improvements replaced the wall-following behavior with a complete traversal mechanism that avoids loops and minimizes path length. The explorer now terminates as soon as it reaches the exit with a reconstructed path, rather than relying on brute-force decisions or visual cues. And reduced the total moves to 128.

##### output :
(maze-runner) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ python main.py --auto --type static
pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Optimized BFS Maze Stats ===
Total time taken: 0.00 seconds
Total moves made: 128
Backtracking: Not applicable (BFS doesn't backtrack)
==================================

Maze solved in 0.00 seconds
Number of moves: 128
Note: Width and height arguments were ignored for the static maze

- and just as a test (not sure if it's allowed) I created a BFS search with path smoothing to reduce the number of movemns to a minmum in (src/BFSExplorer_PathSmoothing.py)

how to run :
python test/test_bfs_explorer_PathSmoothing.py

output :
(maze-runner) student@vg-DSAI-3202-13:~/ParallelAndDistrbutedComp-W2025$ python test/test_bfs_explorer_PathSmoothing.py 
pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html
=== BFS Explorer Test (Static Maze with Path Smoothing) ===

=== Optimized BFS Maze Stats (With Path Smoothing) ===
Total time taken: 0.00 seconds
Total moves made: 30
Backtracking: Not applicable (BFS doesn't backtrack)
==================================

Total time taken : 0.0015 seconds
Total moves made : 30
===========================================================

### Question 5 (20 points)

Compare the performance of your enhanced explorer with the original:
   - Run both versions on the static maze
   - Collect and compare all relevant metrics
   - Create visualizations showing the improvements
   - Document the trade-offs of your enhancements
Your answer should include:
1. Performance comparison results and analysis
2. Discussion of any trade-offs or new limitations introduced

#### Answer
After runinng the original right-hand-rule-based and the new BFS-based explorers on the static maze, i got the following results:
original :
=== Maze Exploration Statistics ===
Total time taken: 0.00 seconds
Total moves made: 1279
Number of backtrack operations: 0
Average moves per second: 747667.57
==================================

bfs:
=== Optimized BFS Maze Stats ===
Total time taken: 0.00 seconds
Total moves made: 128
Backtracking: Not applicable (BFS doesn't backtrack)
==================================

The original explorer completed the maze in 1279 moves while the BFS explorer solved the maze in only 128 moves without backtracking

This shows that BFS guarantees an optimal path. However, BFS does consume more memory due to its need to store visited nodes and reconstruct the shortest path. Despite this, the trade-off is well justified for a better result.

### Final points 6 (10 points)
1. Solve the static maze in 150 moves or less to get 10 points.
2. Solve the static maze in 135 moves or less to get 15 points.
3. Solve the static maze in 130 moves or less to get 100% in your assignment.(done)

### Bonus points
1. Fastest solver to get top  10% routes (number of moves)
2. Finding a solution with no backtrack operations
3. Least number of moves. 
(got 128 moves. (and 30 moves with the test path smoothing(not sure if it's allowed.)))
