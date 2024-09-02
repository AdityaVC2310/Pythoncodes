def two_sum(nums, target):
    num_map = {}  # Dictionary to store the number and its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  # Return indices of the two numbers
        num_map[num] = i  
# User input
nums = list(map(int, input("Enter the numbers in the array, separated by spaces: ").split()))
target = int(input("Enter the target number: "))

# Find and print the indices
result = two_sum(nums, target)
print(f"The indices of the two numbers that add up to {target} are: {result}")
