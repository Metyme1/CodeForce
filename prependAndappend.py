n = int(input())
for _ in range(n):
    m = int(input())
    final = input()
    l = 0
    r = m - 1

    while l < r and final[l] != final[r]:
        l += 1
        r -= 1

    original_length = m - 2 * l
    print(original_length)
