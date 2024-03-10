# Project 10 
# Quiz program

quiz = {
    "question1":{
        "question":"What is the capital city of Bangladesh?",
        "answer":"Dhaka"
    },
    "question2":{
        "question":"What is the capital city of Denmark?",
        "answer":"Copenhagen"
    },
    "question3":{
        "question":"What is the capital city of Japan?",
        "answer":"Tokyo"
    },
    "question4":{
        "question":"What is the capital city of USA?",
        "answer":"Washington"
    },
    "question5":{
        "question":"What is the capital city of Russia?",
        "answer":"Moscow"
    },
    "question6":{
        "question":"What is the capital city of Spain?",
        "answer":"Madrid"
    }
}

# print(quiz)

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print("Your score is " + str(score))
        print("")
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is " + str(score))
        print("")

print("You got " + str(score) + " out of " + str(len(quiz)) + " qustions correctly!")
print("Your percentage is " + str(int(score/len(quiz) *100)) + "% !")
print("Thanks for playing the quiz!\n")
