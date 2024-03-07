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
    else:
        pass

# Continuing...
