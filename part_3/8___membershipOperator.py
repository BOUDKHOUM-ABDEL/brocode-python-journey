

#membership operators = used to test whether value or valiable is found in a sequence
#                     (string , list, turple, or dictionary)
#                     1.in    2.not in

#exemple 1:

word="APPLE"
letter = input("Guess a letter: ").upper()
if letter in word:
    print(f"Yes {letter} is in the word")
else:
    print(f"Sorry {letter} is not in the word")

#exemple 2:
guests = ["Alice", "Bob", "Charlie"]
name = input("Enter your name: ").title()
if name not in guests:
    print("You are not on the guest list")
else:
    print("Welcome to the party!")

#exemple 3: 
grades ={"sandy": "A", "patrick":"B", "Mary":"C"}

student = input("Enter your name: ").lower()
if student in grades:
    print(f"{student.title()} got a {grades[student]}")
else:
    print(f"Sorry {student.title()} you got no grade")