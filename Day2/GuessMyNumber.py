# TASK 1 - Guess My Number
# Level: Beginner | Suggested time: 30-45 minutes
# Can you beat the computer?

# Problem Statement
# Build a number guessing game. The computer secretly selects a number from 1 to 100, and the player tries to guess it.

# Your Mission - Required Features
# . Generate a random number from 1 to 100.
# . Tell the player whether each guess is too high or too low.
# . Count and display the number of attempts.
# . Handle non-numeric input without crashing.

# Bonus Power-Ups
# . Give the player only 7 attempts.
# . Add Easy, Medium, and Hard difficulty levels.
# . Allow the player to play again.

# Sample Output Idea
# You guessed it in 4 attempts! You win!

import random

number = random.randint(1, 100)
attempts = 0
continue_playing = True

while continue_playing:
    print("Welcome to Guess My Number")
    print("Select a difficulty level: Easy (1), Medium (2), Hard (3)")

    difficulty = input("Enter your choice (1, 2, or 3): ")

    if difficulty == '1':
        max_attempts = 10

    if difficulty == '2':
        max_attempts = 7

    if difficulty == '3':
        max_attempts = 5
    
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Your number is too low")
            elif guess > number:
                print("Your number is too high")
            else:
                print(f"You guessed it in {attempts} attempts! You win!")
                break
        except ValueError:
            print("Please enter a valid number.")

    if attempts >= max_attempts:
        print(f"Game over! The number was {number}.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        continue_playing = False