

temp=5
is_sunny=True

if temp>=25 and is_sunny:
    print("It's a hot outside ♨️")
    print("it's sunny ☀️")
elif 0<temp<25 and is_sunny:
     print("It's cold today ❄️")
     print("It's sunny ☀️")
elif temp<=0 or not is_sunny:
    print("It's cold today ❄️")
    print("It's cloudy ☁️")
else:
    print("It's a lovely day 🌤️")

    #conditional statements: and, or , not
num=10
print("positive " if num>0 else "zero" if num==0 else "negative")


user ="admin"
access_level ="full access" if user=="admin" else "limited access" 
print(access_level)