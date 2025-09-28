

item=input("what item would you like to buy?  : ")

price =float(input("Enter the price : "))
quantity=int(input("How many would you like to buy ?   :"))

price_total=price*quantity
print(f"you have bought {quantity}x{item}/s")
print(f"the Total price is {price_total} $")
