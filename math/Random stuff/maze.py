import curses
from curses import wrapper
import queue
import time
import random
from numpy.random import choice

DIFFICULTY = [0.5, 0.5]

# Define the initial maze
maze = [
    ["#", "#", "O", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

block = ["#", " "]
get_colu = int(input("How many columns you want? (9+): ")) - 9
get_rows = int(input("How many rows you want? (9+): ")) - 9

# Adjust the maze height by inserting rows
add = ["#"] + [" "] * 7 + ["#"]
for _ in range(get_rows):
    maze.insert(1, add.copy())  # Use copy to avoid reference issues

# Adjust each row to the new column size and fill each cell randomly
for i in range(len(maze)):
    while len(maze[i]) < (9 + get_colu + 2):
        if i == 0 or i == len(maze) - 1:
            maze[i].insert(-1, "#")
        else:
            for _ in range(get_colu):
                luck = choice(block, p=DIFFICULTY)
                maze[i].insert(-1, luck)

# Sleep function
def sleep(x):
    time.sleep(x)

# Function to shuffle the maze including the start and end positions within their rows
def shuffle_maze(maze):
    for i in range(1, len(maze) - 1):
        row_positions = maze[i][1:-1]  # Exclude corners
        random.shuffle(row_positions)
        maze[i] = ["#"] + row_positions + ["#"]

    # Shuffle start ('O') position within its row
    start_pos = find_start(maze, "O")
    if start_pos:
        start_row, start_col = start_pos
        available_positions = [j for j in range(1, len(maze[start_row]) - 1) if maze[start_row][j] != "#"]
        new_start_col = random.choice(available_positions)
        maze[start_row][start_col] = " "
        maze[start_row][new_start_col] = "O"

    # Shuffle end ('X') position within its row
    end_pos = find_start(maze, "X")
    if end_pos:
        end_row, end_col = end_pos
        available_positions = [j for j in range(1, len(maze[end_row]) - 1) if maze[end_row][j] != "#"]
        new_end_col = random.choice(available_positions)
        maze[end_row][end_col] = " "
        maze[end_row][new_end_col] = "X"

# Function to print the maze
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)

# Function to clear the path
def clear_path(maze, stdscr):
    BLUE = curses.color_pair(1)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j * 2, value, BLUE)

# Function to find the start position
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

# Function to find neighbors of the current position
def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))
    return neighbors

# Function to find the path in the maze
def find_path(maze, stdscr, show_maze=True):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        if show_maze:
            stdscr.clear()
            print_maze(maze, stdscr, path)
            sleep(1.8 / (len(maze)**1.5))
            stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
    
    return None

# Function to retrace the path in white 'X'
def retrace_path(maze, stdscr, path):
    WHITE = curses.color_pair(3)  # Define white color pair
    for position in path:
        row, col = position
        stdscr.addstr(row, col * 2, "X", WHITE)
        stdscr.refresh()
        sleep(0.01)  # Add a short delay to visualize the retracing

# Function to ensure the maze is solvable
def ensure_solvable_maze(maze, stdscr):
    while True:
        shuffle_maze(maze)
        if find_path(maze, stdscr, show_maze=False):
            break

# Main function for the curses application
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Define white color pair

    max_y, max_x = stdscr.getmaxyx()
    maze_height = len(maze)
    maze_width = len(maze[0]) * 2

    if maze_height > max_y or maze_width > max_x:
        stdscr.addstr(0, 0, "The maze is too large for the terminal window.")
        stdscr.refresh()
        stdscr.getch()
        return

    ensure_solvable_maze(maze, stdscr)
    path = find_path(maze, stdscr)
    if path:
        stdscr.clear()
        clear_path(maze, stdscr)
        retrace_path(maze, stdscr, path)
    stdscr.getch()

# Start the curses application
wrapper(main)
