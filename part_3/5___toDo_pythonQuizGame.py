
from mimetypes import guess_all_extensions


questions = ("1. What is the capital of France?", 
             "2. What is 2 % 2?", 
             "3. What is the name of the software that manages a computer's resources?",
             "4. Which of these is a type of computer memory?")

options = (("A.London","B.Paris","C.Rabat","D.Madrid"),
           ("A.0","B.1","C.2","D.4"),
           ("A.Web browser","B.Operating system","C.Antivirus","D.Spreadsheet"),
           ("A.Processor", "B.Graphics card", "C.RAM", "D.Motherboard"))

answers = ("B","A","B","C" )

guesses = []
score=0
question_num=0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ")
    guesses.append(guess.upper())
    
    if guesses[question_num] == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
    print()

print("__________Results__________")
print("Score: " + str(score) + "/" + str(len(questions)))
print("Answers: ", end="")




