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
    return [num1, num2, num3]

# generates three random winning numbers
def get3WinningNum():
    numW1 = random.randint(0,9)
    numW2 = random.randint(0,9)
    numW3 = random.randint(0,9)
    return [numW1, numW2, numW3]

# checks
def checkWinLose(list1, list2):
    if all(elem in list1 for elem in list2):
        print("Winner!")
    else: 
        print("You loss!")

# main
inputNums = ask3Num()
winningNums = get3WinningNum()

# dislay user input and winning numbers 
print(f"Your guesses: {inputNums}\nWinningnumbers: {winningNums}")

# declare win or lose
checkWinLose(inputNums, winningNums)
