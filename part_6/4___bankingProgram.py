


balance=0.0

def show_balance():
    print(f"Your balance is {balance:10.2f}")

def deposit():
    global balance
    amount= float(input("Enter amount to deposit: "))
    if amount >0:
        balance=balance+amount
        print("Deposit successful")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount= float(input("Enter amount to withdraw: "))
    if amount >0:
        if amount <= balance:
            balance=balance-amount
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
    else:
        print("Invalid amount")

is_running=True
while is_running:
    print("\nWelcome to the Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice=input("Enter your choice (1-4): ")
    if choice=="1":
        show_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        is_running=False
        print("Thank you for using the Banking Program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
