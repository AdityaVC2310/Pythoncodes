def group_anagrams(strs):
    # Initialize an empty dictionary to hold the groups of anagrams.
    anagrams = {}
    
    # Iterate over each string in the list.
    for s in strs:
        # Sort the string and use the sorted string as a key.
        sorted_str = ''.join(sorted(s))
        
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    
    # Return the values of the dictionary as a list of lists.
    return list(anagrams.values())

# User input 
def get_user_input():
    strs = []
    print("Enter strings one by one. type 'finish' when you are finished:")
    
    while True:
        user_input = input("Enter a string: ")
        if user_input.lower() == 'finish':
            break
        strs.append(user_input)
    
    return strs

# Main function
def main():
    strs = get_user_input()
    grouped_anagrams = group_anagrams(strs)
    print("Grouped Anagrams:", grouped_anagrams)


if __name__ == "__main__":
    main()
