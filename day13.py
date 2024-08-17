# Create a list of squares using list comprehension with user input
def create_squares_list(input_list):
   
    squares_list = [x**2 for x in input_list]
    return squares_list
def main():
    #  input from the user and converting it into a list of integers
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    squares = create_squares_list(numbers)
    # Display results
    print("Original list:", numbers)
    print("List of squares:", squares)
if __name__ == "__main__":
    main()

