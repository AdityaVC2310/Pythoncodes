#Function Definition

def find_largest_number():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    n3 = float(input("Enter the third number: "))

    largest_number = max(n1,n2,n3)
    print("The largest number is:", largest_number)

# Call the function to execute the program
find_largest_number()
