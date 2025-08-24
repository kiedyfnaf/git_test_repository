import curses
from curses import wrapper
import queue
import time
import random

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
get_colu = int(input("How many columns you want?(9+): ")) - 9
get_rows = int(input("How many rows you want?(9+): "))- 9
add = ["#"] + [" "]*7  + ["#"]
for row in range(get_rows):
    maze.insert(1, add)
for i in range(len(maze)):
    # Adjust each row to the new column size
    while len(maze[i]) < (9 + get_colu + 2):
        if i == 0 or i == len(maze) - 1:
            maze[i].insert(1, "#")
        else:
            maze[i].insert(1, " ")

# Sleep function
for k in range(len(maze)):
    print(maze[k])