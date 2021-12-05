# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

# asks user guess
def getUserGuess():
    userNum = int(input("Enter guess: "))
    return userNum

# checks if number is less than or greater than
def checkNumber(guessNum, winningNum):
    if guessNum > winningNum:
        print("Greater than")
    elif guessNum < winningNum:
        print("Less than")
    else:
        print("Congratulations! You guessed the number!")

# initiates the guessing game
def play(winningNum):
    guessNum = ("")
    while guessNum != winningNum:
        guessNum = getUserGuess()
        checkNumber(guessNum, winningNum)
        continue

# main
# game intro
print("Hello user! Can u guess the secret number?")
print("-----------------------------------------------")

# generates random num
randNum = random.randint(0,100)
play(randNum)

