

#Exeption  = an event that interrupts the flow of a program 
#           (ZeroDivisionError , TypeError , valueError )
#           1.try    2.exept   3.finally


# try:
#     #try some code 
# except Exception:
#     #handle an Exeption
# finally :
#     #do some clean up

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    except TypeError:
        print("Error: Invalid input type. Please use numbers.")

    except ValueError:
        print("Error: Value error occurred.")

    finally:
        print("Execution completed.")

# Example usage
divide_numbers(10, 2)     # Valid division
divide_numbers(10, 0)     # Triggers ZeroDivisionError
divide_numbers("10", 2)   # Triggers TypeError