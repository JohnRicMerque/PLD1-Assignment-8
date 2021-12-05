# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

# asks user guess and validates it
def getUserGuess():
    while True:
        try: 
            userNum = int(input("Enter guess: "))
        except ValueError:
            print("Invalid. Please enter a number")
            continue
        else:
            break
    return userNum

# checks if input number is less than or greater than random number
def checkNumber(guessNum, winningNum):
    if guessNum > winningNum:
        print("Greater than")
    elif guessNum < winningNum:
        print("Less than")
    elif guessNum == winningNum:
        print("-----------------------------------------------")
        print("Congratulations! You guessed the number!")

# runs the guessing game
def play(winningNum):
    guessNum = ("")
    while guessNum != winningNum:
        guessNum = getUserGuess()
        checkNumber(guessNum, winningNum)
        continue
    print(f"[secret number: {winningNum}]")
    print("\n")

# initiates start of game
def start():
    # game intro
    print("-----------------------------------------------")
    print("Hello user! Can u guess the number?")
    print("-----------------------------------------------")
    # generates random num
    randNum = random.randint(0,100)
    play(randNum)

# play again
def playAgain():
    while True:
        yn = input("Play again? y/n: ")
        yn = yn.lower()
        if yn == 'y':
            print("\n")
            start()
        elif yn == 'n':
            print("-----------------------------------------------")
            print("Bye player!")
            break
        else:
            print("Please enter y if you want to play again, or enter n to exit the game.")
            print("\n")
# main
start()
playAgain()