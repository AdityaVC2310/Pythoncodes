def count_characters(string):
    # Create an empty dictionary to store character frequencies
    char_freq = {}

    # Iterate through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in char_freq:
            char_freq[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_freq[char] = 1

    # Return the character frequency dictionary
    return char_freq

# Example usage:
input_string = input("Enter a string: ")
frequency = count_characters(input_string)
print("Character Frequency:")
for char, count in frequency.items():
    print(char, ":", count)