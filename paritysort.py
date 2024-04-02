# Read the number of test cases
t = int(input())

# Initialize a list to store the results
results = []

# Process each test case
for _ in range(t):
    # Read the length of the array (this value is not used directly in the solution, but it's part of the input format)
    n = int(input())
    # Read the array elements
    arr = list(map(int, input().split()))

    # Separate and sort even and odd numbers
    evens = sorted([x for x in arr if x % 2 == 0])
    odds = sorted([x for x in arr if x % 2 != 0])

    # Rebuild the array, placing even and odd numbers in their original positions
    sorted_arr = []
    for num in arr:
        # Append the next even or odd number in the sorted sequence
        if num % 2 == 0:
            sorted_arr.append(evens.pop(0))
        else:
            sorted_arr.append(odds.pop(0))

    # Check if the rebuilt array is sorted
    if sorted_arr == sorted(arr):
        results.append("YES")
    else:
        results.append("NO")

# Output the results
for result in results:
    print(result)
