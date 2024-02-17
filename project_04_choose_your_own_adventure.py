name = input("Type your name? ")
print("Welcome", name, "to this adventure!")
print("----------")

answer = input('''You are on a dirt road, 
it has come to an end and 
you can go left or right. 
Which way would you like to go? ''').lower()
print("----------")

if answer == "left":
    answer = input('''You come to a river, 
you can walk around it 
or you can swim across? 
Type walk to walk around 
or swim to swim across: ''').lower()

    if answer == "walk":
        print("Walking...")
    elif answer == "swim":
        print("Swimming...")
    else:
        print("Not a valid option, you lost.")

elif answer == "right":
    print("You chosed to go right")
else:
    print("Not a valid option, you lost.")
