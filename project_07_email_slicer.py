# Project 7
# Email Slicer

def main():
    print("Welcome to the email slicer.")
    print("")

    email_input = input("Input your email: ").lower()

    username, domain = email_input.split("@")
    domain, extension = domain.split(".")

    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension, "\n")

while True:
    main()
    x = input("Continue(c) or exit(e) the program? ").lower()
    if x == "e":
        print("Program closed successfully.")
        quit()
    elif x == "c":
        continue
