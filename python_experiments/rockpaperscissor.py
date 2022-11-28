# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock


from itertools import product

def game_human():
    choice = ("rock", "scissor", "paper")
    comb = list(product(choice, choice))
    draw = [e for e in comb if e[0] == e[1]]
    rest = [e for e in comb if e not in draw]
    win1 = [rest[0], rest[3], rest[4]]
    win2 = [e for e in rest if e not in win1]

    print("Player 1 turn")
    one = input(f"Write rock, scissor, paper: ")

    print("Player 2 turn")
    two = input(f"Write rock, scissor, paper: ")
    if one and two not in choice:
        raise ValueError("Insert a valid choice")

    match = (one, two)

    print(f"Aaaaaaand the winner is......")
    print(f"You want to know it?")
    print(f"I'll tell you then!")
    print(f"Sure i'll do!")
    print(f"is.......")
    print(f"the magnificent.........")
    if match in win1:
        winner = "Player 1!!!"
    elif match in win2:
        winner = "Player 2!!!"
    elif match in draw:
        winner = "It's actually a DRAW!!!"
    print(winner)
