#simple_word_replacement_program

def replace_word():

    str = "Hi, I am Zaber, hey hey hey!"
    print(str)
    print("----------")

    word_to_replace = input("Enter the word to replace? ")
    new_word = input("Enter the new word? ")
    print("----------")
    print(str.replace(word_to_replace, new_word))

replace_word()
