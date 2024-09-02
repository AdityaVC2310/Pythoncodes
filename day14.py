# Function to convert a single digit into its corresponding alphabet
def number_to_alphabet(number):
    # Convert number to the corresponding alphabet
    return chr(number + 64)

# Function to combine numbers into a word
def numbers_to_word(numbers):
    word = ''
    for num in numbers:
        word += number_to_alphabet(num)
    return word

# Take numbers from the user
numbers_input = input("Enter numbers separated by spaces (between 1 and 26): ")

# Split the input string into a list of strings
numbers = [int(num) for num in numbers_input.split()]

# Generate the word
word = numbers_to_word(numbers)

# Print the result
print(f"The word is: {word}")
