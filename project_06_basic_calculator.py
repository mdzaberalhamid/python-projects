# Project 6
# Basic Calculator
# Must have functions: add, sub, mul, div

def add(a, b):
    answer = a + b
    print("Result of " + str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print("Result of " + str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print("Result of " + str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print("Result of " + str(a) + " / " + str(b) + " = " + str(answer) + "\n")

# test functions
# add(4, 3)
# sub(6, 1)
# mul(3, 3)
# div(8, 2)

while True:

    # print("")
    print("Basic Calculator")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    print("----------")
    choice = input("Input your choice: ")

    if choice == "A" or choice == "a":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)
    elif choice == "B" or choice == "b":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)
    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)
    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("input second number: "))
        div(a, b)
    elif choice == "E" or choice == "e":
        print("Program ended.")
        quit()
    else:
        print("Invalid input, program ended.")
        quit()
