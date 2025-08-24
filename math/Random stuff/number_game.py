import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("How many players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be (2-4).")
    else:
        print("Wrong, invalid input.")

max_score = 50
player_scores =[0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range (players):
        print("\nPlayer: ", player_idx + 1, "turn.\n")
        print("Total score:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Roll (y): ")
            if should_roll.lower() != "y":
                break
            value = roll()

            if value == 1:
                print("You hit 1.")
                current_score = 0
                break
            else:
                current_score += value
                print("You got a: ", value)
            print("Your score is: ", current_score)
        player_scores[player_idx] += current_score
        print("Total: ", player_scores[player_idx])
max_score = max(player_scores)
winning_ind = player_scores.index(max_score)
print("Player", winning_ind + 1, "has won with the score:", max_score)