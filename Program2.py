# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

# generates random num
randNum = random.randint(0,100)

# asks user guess
def getUserGuess():
    userNum = int(input("Guess the number. Enter here: "))
    return userNum

# checks if number is less than or greater than
def checkNumber(guessNum, winningNum):
    if guessNum > winningNum:
        print("Greater than")
    else:
        print("Less than")
