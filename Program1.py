# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

# asks user for three numbers
def ask3Num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    uList = [num1, num2, num3]
    return uList

# generates three random winning numbers
def get3WinningNum():
    numW1, numW2, numW3 = random.sample(range(0, 9), 3)
    wList = [numW1, numW2, numW3]
    return wList

# checks
def checkWinLose(list1, list2):
    if sorted(list1) == sorted(list2):
        print("Winner!")
    else: 
        print("You loss!")

# initiates the game 
def play():
    print("-----------------------------")
    print("Welcome to the Lottery")
    print("-----------------------------")
    # asks user 3 numbers and generates 3 winning numbers
    inputNums = ask3Num()
    winningNums = get3WinningNum()
    # dislay user input and winning numbers
    print("-----------------------------") 
    print(f"Your guesses: {inputNums}\nWinning numbers: {winningNums}")
    # declare win or lose
    print("-----------------------------") 
    print("RESULT") 
    checkWinLose(inputNums, winningNums)
    print("-----------------------------")

# asks user to play again
def playAgain():
    while True:
        yn = input("Try again? y/n: ")
        yn = yn.lower()
        if yn == 'y':
            play()
        elif yn == 'n':
            print("-----------------------------")
            print("Bye player!")
            break
        else:
            print("\n")
            print("Please enter y if you want to play again, enter n to exit the game.")
# main
play()
playAgain()

