# Project 14 
# Dice Rolling Simulator

# Step 1 - import random module
# Step 2 - defining a function to roll the dice
# Step 3 - create a dictionary that will have the values of the dice

import random

def roll_dice():
    roll = input("Roll the dice? (Yes/No): ")

    dice_drawings = {
        1: (
            " _______",
            "|       |",
            "|   1   |",
            "!_______!"
        ),
        2: (
            " _______",
            "|       |",
            "|   2   |",
            "!_______!"
        ),
        3: (
            " _______",
            "|       |",
            "|   3   |",
            "!_______!"
        ),
        4: (
            " _______",
            "|       |",
            "|   4   |",
            "!_______!"
        ),
        5: (
            " _______",
            "|       |",
            "|   5   |",
            "!_______!"
        ),
        6: (
            " _______",
            "|       |",
            "|   6   |",
            "!_______!"
        )
    }

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawings[dice1]))
        print("\n".join(dice_drawings[dice2]))

        roll = input("\nRoll again? (Yes/No): ")

roll_dice()
