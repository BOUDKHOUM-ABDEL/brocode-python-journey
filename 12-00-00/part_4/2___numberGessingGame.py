
import random
low = 1
high = 100
number = random.randint(low,high)
tries=0

while True:
    guess=int(input("Enter a number between 1 and 100: "))
    if guess < low or guess > high:
        print("Invalid input. Please try again.")
        continue
    tries += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {tries} tries.")
        break

    