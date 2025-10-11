
#format specifiers = special characters = {value:flags} format a value based on what flags are inserted

#.(number)f: specifies the number of decimal places to display for a floating-point number
#:(number) = allocate that many spaces 
#:03 = allocate and zero pad that many sapaces 
#:< = left justify
#:> = right justify
#:^ = center align
#:+ = use a plus sign to indicate a positive value
#:= = place sign to leftmost position 
#:  = insert a space before positive number 
#:, = comma separator\

# price1=3.14656
# price2= 98765.4321
# price3=12.34
# print(f"Price1: {price1:.2f}") #round to 2 decimal places
# print(f"price2:{price2: 09}") #allocate 9 spaces and pad with zeros space for sign
# print(f"price3:{price3:<10}") #allocate 10 spaces and left justify
# print(f"price2:{price2: ,}") #comma separator for thousands
# print(f"price2:{price2:+ ,.3f}") #comma separator and round to 3 decimal places, space for sign")

price1 = 3.14656
price2 = 98765.4321  # Use a float, not a tuple
price3 = 12.34
print(f"Price1: {price1:.3f}")  # round to 2 decimal places
print(f"price2:{price2: 09}")   # allocate 9 spaces and pad with zeros space for sign
print(f"price3:{price3:<10}")   # allocate 10 spaces and left justify
print(f"price2:{price2:,}")     # comma separator for thousands
print(f"price2:{price2:+,.3f}") # comma separator and round to 3 decimal places, space for sign