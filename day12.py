def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second

# Get user input
n = int(input("Enter the number of steps: "))

# Calculate and display the number of ways to climb the staircase
if n > 0:
    print(f"Number of ways to climb to the top of {n} steps:", climbStairs(n))
else:
    print("Please enter a positive integer.")
