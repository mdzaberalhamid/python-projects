# Project 16 
# Currency Converter

def main():
    print("This program converts US dollars to Pound Sterling.")
    print("")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "Pounds.")

convert_to_pounds = lambda dollars: dollars * 0.82

main()

exit = input("\nPress any key to quit...")
quit()
