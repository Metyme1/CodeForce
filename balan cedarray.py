n = int(input())
for _ in range(n):
    m = int(input())
    k = m // 2
    if k % 2 != 0:
        print("NO")
    else:
        # Prepare the arrays for even and odd values
        evens = []
        odds = []
        # Even numbers
        for j in range(1, m + 1):
            if j % 2 == 0:
                evens.append(j)
            else:
                odds.append(j)

        # Adjust the last odd to balance the sums
        odds[-1] += k

        print("YES")
        print(" ".join(map(str, evens + odds)))
