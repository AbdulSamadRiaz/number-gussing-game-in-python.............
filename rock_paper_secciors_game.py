
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(
        "Type rock, paper, scissors or Q to quit: "
    ).lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(options)

    print("Computer chose:", computer_choice)

    if user_input == computer_choice:
        print("It's a draw!")

    elif (
        (user_input == "rock" and computer_choice == "scissors")
        or (user_input == "paper" and computer_choice == "rock")
        or (user_input == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Goodbye!")