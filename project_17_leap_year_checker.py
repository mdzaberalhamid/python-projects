# Project 17 
# Leap Year Checker

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year!")
            else:
                print("Not Leap Year!")
        else:
            print("Leap Year!")
    else:
        print("Not Leap Year.")

print("Leap Year Checker\n")
year = int(input("Enter year: "))

is_leap_year(year)

q = input("Press any key to quit...")
quit()
