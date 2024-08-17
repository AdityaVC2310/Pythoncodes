# Function to check if a string is a palindrome
def is_palindrome(s):
    
    
    return s == s[::-1]

# Input string from the user
input_string = input("Enter a string: ")

# Check and print whether the string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
