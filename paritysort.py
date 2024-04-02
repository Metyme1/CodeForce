t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    evens = sorted([x for x in arr if x % 2 == 0])
    odds = sorted([x for x in arr if x % 2 != 0])

    sorted_arr = []
    for num in arr:

        if num % 2 == 0:
            sorted_arr.append(evens.pop(0))
        else:
            sorted_arr.append(odds.pop(0))

    if sorted_arr == sorted(arr):
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
