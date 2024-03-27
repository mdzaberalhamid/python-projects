# Project 19 
# Word Dictionary 2

from PyDictionary import PyDictionary

dictionary = PyDictionary()

# print(dictionary.meaning("eyes"))

while True:

    word = input('\nEnter your word: ')

    if word == "":
        break

    print(dictionary.meaning(word))
