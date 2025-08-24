import random

# Initial maze definition
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

# Randomize the first row ensuring "O" isn't in the corners
first_row_positions = maze[0][1:8]  # Exclude corners
random.shuffle(first_row_positions)
maze[0] = ["#"] + first_row_positions[:7] + ["#"]

# Randomize the last row ensuring "X" isn't in the corners
last_row_positions = maze[8][1:8]  # Exclude corners
random.shuffle(last_row_positions)
maze[8] = ["#"] + last_row_positions[:7] + ["#"]

# Print the randomized maze
for row in maze:
    print("".join(row))
