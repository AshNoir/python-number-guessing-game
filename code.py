"""
================================
NUMBER GUESSING GAME
================================
Select Difficulty
1. Easy   → 1-50
2. Medium → 1-100
3. Hard   → 1-500

Enter 's' to start and anything else to stop.
"""

import random


# Game Over message
o = """
================================
GAME OVER
================================
"""


# Display the game menu
print("""
================================
NUMBER GUESSING GAME
================================
Select Difficulty
1. Easy   → 1-50
2. Medium → 1-100
3. Hard   → 1-500

Enter 's' to start and anything else to stop.
""")


# Main program loop
while True:

    # Ask the user whether they want to start the game
    st = input("Enter s to start: ").lower()

    # Start the game if the user enters 's'
    if st == "s":

        # Ask the user to select a difficulty
        diff = int(input("Select Difficulty level: "))

        # ---------------- EASY MODE ----------------
        if diff == 1:

            # Generate a random number between 1 and 50
            a = random.randint(1, 50)

            print("I have selected a number between 1 and 50")

            # Keep track of the number of attempts
            total = 0

            # Keep asking until the user guesses correctly
            while True:

                guess = int(input("Enter the number: "))

                # Increase attempt count
                total += 1

                # Check if the guess is correct
                if guess == a:

                    print("Congrats :)")
                    print(f"You guessed the number in {total} attempts.")
                    print(o)

                    # Exit the guessing loop
                    break

                # Guess is greater than the random number
                elif guess > a:
                    print("Too High :(")

                # Guess is smaller than the random number
                else:
                    print("Too Low :(")


        # ---------------- MEDIUM MODE ----------------
        elif diff == 2:

            # Generate a random number between 1 and 100
            b = random.randint(1, 100)

            print("I have selected a number between 1 and 100")

            # Keep track of attempts
            total = 0

            while True:

                guess = int(input("Enter the number: "))

                total += 1

                # Correct guess
                if guess == b:

                    print("Congrats :)")
                    print(f"You guessed the number in {total} attempts.")
                    print(o)

                    break

                # Guess is too high
                elif guess > b:
                    print("Too High :(")

                # Guess is too low
                else:
                    print("Too Low :(")


        # ---------------- HARD MODE ----------------
        elif diff == 3:

            # Generate a random number between 1 and 500
            c = random.randint(1, 500)

            print("I have selected a number between 1 and 500")

            # Keep track of attempts
            total = 0

            while True:

                guess = int(input("Enter the number: "))

                total += 1

                # Correct guess
                if guess == c:

                    print("Congrats :)")
                    print(f"You guessed the number in {total} attempts.")
                    print(o)

                    break

                # Guess is too high
                elif guess > c:
                    print("Too High :(")

                # Guess is too low
                else:
                    print("Too Low :(")


        # If the user enters something other than 1, 2 or 3
        else:
            print("Invalid Option.")


    # Anything other than 's' stops the session
    else:
        print("The Session got killed.")
        break
