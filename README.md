🎯 Number Guessing Game

A fun and interactive Python console game where the computer randomly selects a number, and the player tries to guess it.
It’s a great beginner project to learn about loops, conditionals, and random number generation in Python.

🧩 Project Overview

In this game, the computer picks a secret number between 1 and 100.
The player keeps guessing until they find the correct number, with hints provided after each guess:

🔼 Too low! → Guess higher

🔽 Too high! → Guess lower

🎉 Correct! → You found the number!

At the end, the program shows how many attempts it took and gives an option to play again.

🧠 Concepts Used

This project is perfect for beginners learning:

while loops for repetition

if-elif-else conditionals for logic

random.randint() for number generation

try...except for input validation and error handling

Function-based structure for reusability

🕹️ How to Play

Run the game:

python number_guess.py


Enter your guesses until you find the right number.

The program will tell you if your guess is too high or too low.

Once you win, you can choose to play again or exit.

⚙️ Requirements

Python 3.x

No external libraries needed (only uses the built-in random module)

🚀 Features

✅ Random number generation (1–100)
✅ Unlimited guesses until correct
✅ Input validation (handles non-numeric inputs)
✅ Replay option after winning
✅ Clear feedback messages for each guess

🌟 Example Output
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 45
Too low! Try again ⬆️

Enter your guess: 72
Too high! Try again ⬇️

Enter your guess: 66
🎉 Correct! You got it in 3 attempts.

Do you want to play again? (y/n):

💡 Future Enhancements

You can improve this project later by adding:

Difficulty levels (Easy/Hard)

Limited number of attempts

Scoreboard or high score tracking

Colorful console output (using colorama)

GUI version using Tkinter

🧑‍💻 Author

Developed with ❤️ in Python by P.Lasya Bhavyasri
