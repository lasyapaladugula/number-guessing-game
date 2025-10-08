# number_guess.py
"""
Number Guessing Game
--------------------
The computer picks a random number between 1 and 100.
The player guesses until they get it right.
"""

import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check guess
            if guess < number:
                print("Too low! Try again ⬆️")
            elif guess > number:
                print("Too high! Try again ⬇️")
            else:
                print(f"🎉 Correct! You got it in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("❌ Please enter a valid number!")

    # Ask to play again
    again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if again == "y":
        play_game()
    else:
        print("Thanks for playing! 👋")

if __name__ == "__main__":
    play_game()
