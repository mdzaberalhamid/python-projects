# Project 18 
# Word Dictionary

# Step 1 - create a dictionary that has a key/value pair that represents a word and its meaning
# Step 2 - collect input from a user, input is a word
# Step 3 - check if the word is in the dictionary
# Step 4 - print the definition

print("Word Dictionary")

def main():
    word_dictionary = {
        "hi":"a way of greeting",
        "eyes":"an organ for seeing",
        "earth":"a planet in space",
        "chess":"a popular board game"
    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

    # print(word_dictionary)

main()

# Continuing...
