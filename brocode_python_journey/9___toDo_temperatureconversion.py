
#temperature program conversion

unit=input("Enter the unit you want to convert from (C/F): ")
temp=float(input("Enter the temperature you want to convert: "))

if unit=="C" or unit=="c":
    converted=round((temp*9/5)+32,2)
    print(f"{temp}C is {converted}F")

elif unit=="F" or unit=="f":
    converted=round((temp-32)*5/9,2)
    print(f"{temp}F is {converted}C")
else:
    print("Invalid unit. Please enter C or F.")


