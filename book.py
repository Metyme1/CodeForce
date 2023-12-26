def max_books(n, m, arr):
    l = 0
    max_ = 0
    current_time = 0

    for r in range(n):
        current_time += arr[r]
        while current_time > m:
            current_time -= arr[l]
            l += 1
        max_ = max(max_, r - l + 1)

    return max_


n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(max_books(n, m, arr))
