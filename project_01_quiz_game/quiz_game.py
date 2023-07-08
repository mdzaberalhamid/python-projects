print("")
print("Welcome to the computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okey! Let's Play:)")
score = 0

answer = input("\nWhat does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stands for? ").lower()
if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("\nYou got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

print("\nThanks for playing!")
