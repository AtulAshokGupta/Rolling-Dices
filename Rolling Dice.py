# importing module for random number generation
import random

# range of the values of a dice
min_value = 1
max_value = 6

# to loop the rolling through user input
roll_again = "yes"

# loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are:")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(min_value, max_value))

    # generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_value, max_value))

    # asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Do you want to Roll the Dices Again?")