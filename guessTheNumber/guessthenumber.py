# Write your code here :-)
import random

print("I am thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)

while True:
    for guessesTaken in range(1, 7):
        print("Take a guess")
        guess = int(input())
        if guess > secretNumber:
            print("Your guess is too high")
        elif guess < secretNumber:
            print("Your guess is too low")
        else:
            print(
                "Good work, you got it right! You guessed right in "
                + str(guessesTaken)
                + " tries."
            )
            break
    print("The number I was thinking of was " + str(secretNumber) + ".")
    choice = input("Play again? yes/no: ")
    if choice == "no":
        print("Thank you for playing!")
        break
    elif choice == "yes":
        secretNumber = random.randint(1, 20)
        print("Let's see what you've got")
        print("I am thinking of a number between 1 and 20")
        continue
