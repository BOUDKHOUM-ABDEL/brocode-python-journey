

import random

options=["rock","paper","scissors"]

computer_wins=0
player_win=0

print("___________Welcome to Rock, Paper, Scissors____________")
print("You will be playing against the computer. Best of 3 wins!")
print("-------------------------------------------------------\n")
while not (computer_wins==3 or player_win==3):
    computer_option=random.choice(options)
    player_option=input("Enter rock, paper, or scissors: ").lower()

    if player_option in options:
         print(f"_______ {computer_option} vs {player_option}_______")

    
         if player_option==computer_option:
          print("It's a tie!")
         elif (player_option=="rock" and computer_option=="scissors") or \
          (player_option=="paper" and computer_option=="rock") or \
         (player_option=="scissors" and computer_option=="paper"):
             print("You win this round!")
             player_win += 1
         else:
             print("Computer wins this round!")
             computer_wins += 1
    else: pass
    print(f"Score - You | {player_win} : {computer_wins} | Computer")
    print("----------------------------------")
    print()

print("______you win!_______ " if player_win==3 else "______Computer wins!_______")