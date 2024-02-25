# Project 6
# Basic Calculator
# Must have functions: add, sub, mul, div

def add(a, b):
    answer = a + b
    print("Result of " + str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

# test functions
# add(4, 3)
# sub(6, 1)
# mul(3, 3)
# div(8, 2)

print("Basic Calculator")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("----------")
choice = input("Input your choice: ")

if choice == "A" or choice == "a":
    print("Addition")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    add(a, b)

# Continuing...
