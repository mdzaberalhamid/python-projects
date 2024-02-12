# Project 02
# Number Guessing Game

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Please, type a number next time!")
    quit()

#r = random.randrange(-5, 11)   # -5 to 10
#r = random.randrange(11)       # 0 to 10
#r = random.randint(0, 11)      # 0 to 11
#print(r)

random_number = random.randrange(0, top_of_range)
print(random_number)

while True:
    user_guess = input("Type a guess? ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please, type a number next time!")
        continue

    if user_guess == random_number:
        print("You got it.")
        break
    else:
        print("You got it wrong.")
