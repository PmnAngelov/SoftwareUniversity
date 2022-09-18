import random

def game():

    human = input("Please make your choice: (r) for rock, (p) for paper, (s) for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if computer == 'r':
        print(f"Computer chooses rock")
    elif computer == 'p':
        print(f"Computer chooses paper")
    else:
        print(f"Computer chooses scissors")

    if human == computer:
        print("It's a tie!")
        # r > s ; s > p ; p > r
    elif human == 'r' and computer == 's' or human == 's' and computer == 'p' or human == 'p' and computer == 'r':
        print('You win')
    else:
        print("You lost")

game()
