print("Program Starts")

try:
    # user input two numbers
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: ")) 

    # perform division
    res = n1 / n2
    
    # display the result
    print("Division = ", res)

except ZeroDivisionError:
    print("Error!!!!, division by zero is not possible")
except ValueError:
    print("Error!!!!, invalid input, please enter a number")
except Exception as obj:
    print(f"Unknown error: {obj}")
else:
    print('No errors detected')
finally:
    print('Inside Finally')

print("Program Ends")
