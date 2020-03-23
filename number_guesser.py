import random


print("Hello, try and guess my number between 1 and 20")
print("You have 6 tries ...")


computer_guess = random.randint(1, 20)

for guesses_taken in range(1, 7):
    human_guess = int(input("What is your guess ?   "))

    if human_guess == computer_guess:
        print()
        break

    elif human_guess > computer_guess:
        print("Too high !")
        print()
        continue

    elif human_guess < computer_guess:
        print("Too low !")
        print()
        continue

if human_guess == computer_guess:
    print("You won with only", guesses_taken,"guesses.")

else:
    print("You lost ...")
