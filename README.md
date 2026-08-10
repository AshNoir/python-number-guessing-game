# python-number-guessing-game
🎯 Python Number Guessing Game

A simple Number Guessing Game built with Python using the random module.

The player chooses a difficulty level, and the program randomly generates a number within the selected range. The player keeps guessing until they find the correct number.

🎮 Features
Three difficulty levels
Random number generation using Python's random module
Attempt counter
"Too High" and "Too Low" hints
Simple command-line interface
Option to start or stop the game
📊 Difficulty Levels
Difficulty	Number Range
Easy	1 - 50
Medium	1 - 100
Hard	1 - 500
🖥️ Example
================================
NUMBER GUESSING GAME
================================

Select Difficulty
1. Easy   → 1-50
2. Medium → 1-100
3. Hard   → 1-500

Enter s to start and anything else to stop.

Enter s to start: s
Select Difficulty level: 1

I have selected a number between 1 and 50

Enter the number: 25
Too Low :(

Enter the number: 40
Too High :(

Enter the number: 34
Congrats :)

You guessed the number in 3 attempts.

================================
GAME OVER
================================
🛠️ Concepts Practiced

This project was created to practice basic Python programming concepts:

random module
random.randint()
while loops
if / elif / else
break
input()
Type conversion using int()
Variables
String formatting using f-strings
Nested loops and conditional statements
▶️ How to Run

Make sure Python is installed on your system.

Clone the repository:

git clone https://github.com/YOUR-USERNAME/python-number-guessing-game.git

Go into the project directory:

cd python-number-guessing-game

Run the program:

python number_guessing_game.py
🚀 Future Improvements

Possible improvements for future versions:

Add input validation
Prevent guesses outside the selected range
Add a maximum number of attempts
Add a scoring system
Add replay functionality
Improve the terminal UI
Refactor repeated code using functions
📚 What I Learned

This project helped me practice Python control flow and the random module by building a small interactive game from scratch.

More improvements will be added as I learn new Python concepts.
