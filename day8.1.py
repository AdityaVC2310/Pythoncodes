def swap_and_combine_strings(string1, string2):
    # Swap the first two characters of each string
    modified_string1 = string2[:2] + string1[2:]
    modified_string2 = string1[:2] + string2[2:]

    # Combine the modified strings with a space separator
    combined_string = modified_string1 + ' ' + modified_string2

    # Return the combined string
    return combined_string

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = swap_and_combine_strings(string1, string2)
print("Modified String:", result)

