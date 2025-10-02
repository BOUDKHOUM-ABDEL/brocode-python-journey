
#match - case = switch - case (other languages)


day=input("What day is it today? ").lower()

match day:
    case "saturday" |"sunday":
        print("It's the weekend!")
    case "monday" |"tuesday" |"wednesday" |"thursday" |"friday":
        print("It's a weekday")
    case _:
        print("Not a valid day")