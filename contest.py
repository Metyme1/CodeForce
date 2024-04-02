# n, m = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# max_t = 0
# diff = 0
# for i in range(len(arr) - 1):
#     diff = arr[i] - arr[i + 1]
#     max_t = max(max_t, diff)

# print(max_t - m)


n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

if len(arr) == 1:
    max_t = 0
else:
    max_t = 0
    diff = 0
    for i in range(len(arr) - 1):
        diff = arr[i] - arr[i + 1]
        max_t = max(max_t, diff)

profit = max_t - m
if profit < 0:
    profit = 0
print(profit)
