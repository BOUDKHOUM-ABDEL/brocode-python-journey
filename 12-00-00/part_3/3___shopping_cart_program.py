
foods=[]
prices=[]
total=0

while True:
	food=input("Enter a food would you like to buy ('q' to finish): ")
	if food.lower() == 'q':
		break

	else:
		price=float(input(f"Enter the price of {food}: $"))
		foods.append(food)
		prices.append(price)
		total += price
	    

print("___________Your Shopping Cart:_____________")
for i in range(len(foods)):
	print(f"{foods[i]}: ${prices[i]:.2f}")
print(f"Total: ${total:.2f}")
print("Thank you for shopping with us!")