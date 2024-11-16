import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter a number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players!")
    else:
        print("Incorrect value!")

max_score = 50
player_scores = [0 for player in range(players)]

while max(player_scores) < max_score:
    for item in range(len(player_scores)):
        print("------------------------------------------------")
        print("\nThe", item + 1, "player's turn\n")
        while True:
            choice = input("Would you roll? (y)es or (n)o\n")
            if choice.lower() != "y":
                break
            else:
                value = roll()
                if value == 1:
                    player_scores[item] = 0
                    print("ROLLED 1 :(\nTotal score reset to zero)")
                    break
                else:
                    player_scores[item] += value
                    print("ROLLED:", value)

        print("Total score:", player_scores[item])


winner_index = player_scores.index(max(player_scores))
print(
    "Congratulations!!!\nPlayer number",
    winner_index + 1,
    "is a -WINNER- with score",
    player_scores[winner_index],
)
