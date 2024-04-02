n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
l = 0
max_x = 0
min_x = 0
smaller = 0
arr2 = []
while n < len(arr):
    arr2 = arr[l:n]

    max_x = max(arr2)
    min_x = min(arr2)
    diff = max_x - min_x
    smaller = min(smaller, diff)
    l += 1
    n += 1
print(smaller)
