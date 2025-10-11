
menu ={"hot Dog": 3.50,
	   "hamburger": 4.00,
	   "fries": 2.00,
	   "soda": 1.50,
	   "water": 1.00 }

orders = []
total = 0.0

print("------ Concession Stand Menu -----")
for item, price in menu.items():
	print(f"{item :10} :  ${price:.2f}")

print("----------------------------------")

while True:
	order = input("Enter an item to order (or 'q' to finish): ").lower()
	if order == 'q':
		break
	elif order in menu:
		orders.append(order)
		total += menu[order]
		print(f"Added {order} to your order. ")
	else:
		print("Sorry, we don't have that item. Please choose from the menu.")

print("----------------------------------")

print("________Your order summary_________:")
for item in orders:
    print(f"- {item :10} :  ${menu[item]:.2f}")
		
print(f"Your final total is: ${total:.2f}")
print("----------------------------------")
print("Thank you for your order!")
