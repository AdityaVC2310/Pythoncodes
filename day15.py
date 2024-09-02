def get_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

# Example usage
my_list = [1, 2, 3, 2, 4, 3, 5,7,7,8,4,3,3,1,1,2,3,9,10]
frequency = get_frequency(my_list)
print("Frequency:", frequency)
