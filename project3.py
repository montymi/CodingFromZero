import random

def guessTheNumber():
    # Generate a random number within a specified range
    min_num = 1
    max_num = 20
    secret_num = random.randint(min_num, max_num)

    # Prompt the user to guess the number
    guess = None
    while guess != secret_num:
        guess = int(input(f"Guess a number between {min_num} and {max_num}: "))

        # Check if the guess is correct
        if guess == secret_num:
            print("Congratulations! You guessed the number.")
            return
        elif guess < secret_num:
            print("The number is higher.")
        else:
            print("The number is lower.")

# Play the game
guessTheNumber()
