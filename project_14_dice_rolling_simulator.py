# Project 14 
# Dice Rolling Simulator

# Step 1 - import random module
# Step 2 - defining a function to roll the dice
# Step 3 - create a dictionary that will have the values of the dice

import random

def roll_dice():
    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

# Continuing...
