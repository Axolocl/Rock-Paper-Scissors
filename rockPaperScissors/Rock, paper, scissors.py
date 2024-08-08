import random

choices = ["rock", "paper", "scissors"]

print("Let's play rock, paper, or scissors")

while True:
    computer_choice = random.choice(choices)
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    print(f"Computer chose: {computer_choice}")

    if player_choice not in choices:
        print("Invalid choice. Please choose again.")
        continue

    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        winner = "Player"
    elif player_choice == computer_choice:
        winner = "Tie"
    else:
        winner = "Computer"

    if winner == "Player":
        print("You won!")
    elif winner == "Computer":
        print("Computer won")
    else:
        print("It's a tie")

    choice = input("Play again? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you for playing!")
        break
