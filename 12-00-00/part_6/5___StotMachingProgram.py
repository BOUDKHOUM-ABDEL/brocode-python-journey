
import random

def spin_row():
    Symbols =[ '🍒', '🍉' , '🍋' , '🔔' , '🌟'  ]
    result=[]
    for symbol in range(3):
        result.append(random.choice(Symbols))
    return result

def print_row(row):
    print(" | ".join(row))

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
       if row[0] == '🍒':
            return bet * 100
       elif row[0] =='🍉':
            return bet * 400
       elif row[0] =='🍋':
            return bet * 500
       elif row[0] =='🔔':
            return bet * 1000
       elif row[0] =='🌟':
            return bet * 2000
    return 0
     
    

def main():
  
    balance=1000

    print("******************************************************")
    print("             Welcome to the Python Slots!             ")
    print("           Symbols : 🍒 , 🍉 , 🍋 , 🔔 , 🌟         ")
    print("******************************************************")


    while balance > 0:
        print(f"\nCurrent Balance: ${balance:.2f}")
        
        bet = (input("Enter your bet amount : $"))
        if  not bet.isdigit():
            print("Invalid input. Please enter a positive number.")
            continue
        bet = int(bet)
        if bet >balance:
            print("Insufficient balance. Please enter a lower bet amount.")
            continue
        if bet <= 0:
            print("bet must be greater than zero.")
            continue
        balance -= bet 
        row = spin_row()
        print ("************spinning...************")
        print_row(row)
        payout=get_payout(row,bet)
        if payout >0:
            print(f"Congratulations! You won ${payout:.2f} ")
            balance += payout
        else:
            print("Sorry, you lost this round.")

        play_again=input(" Enter 'yes' to spin again? (y): ").lower()
        if play_again != 'y' and play_again != 'yes':
            break
        
    if balance <= 0:
        print("You have run out of balance. Game over!")
    else :
        print("************Game Over!************")
        print(f" you cashed out with ${balance:.2f}. Thanks for playing!")








if __name__ == "__main__":
    main()