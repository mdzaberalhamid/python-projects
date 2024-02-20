name = input("Type your name? ")
print("Welcome", name, "to this adventure!")
print("----------")

answer = input('''You are on a dirt road, 
it has come to an end and 
you can go left or right. 
Which way would you like to go? ''').lower()
print("----------")

if answer == "left":
    answer = input("You come to a river, you can walk around it or you can swim across? Type walk to walk around or swim to swim across: ").lower()

    if answer == "walk":
        print("You walked for many miles, run out of water and you lost the game.")
    elif answer == "swim":
        print("You swam across and were eaten by an aligator.")
    else:
        print("Not a valid option, you lost.")

elif answer == "right":
    answer = input("You come to a bridge, it looks like rusty. Do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose the game eventually because you can't survive after choosing to go left.")
    elif answer == "cross":
        print("----------")
        answer = input("You crossed the bridge and met a stranger. Do you want to talk (yes/no)? ")

        print("----------")
        if answer == "yes":
            print("You talked to the stranger and got some gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger and he is offended, so you LOSS.")
        else:
            print("...")

    else:
        print("Not a valid option, you lost.")
    
else:
    print("Not a valid option, you lost.")

print("##########")
print("Thank you for trying, " + name + "!")
