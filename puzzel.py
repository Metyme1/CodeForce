n, m = list(map(int, input().split()))
joy = 0
f = -float("inf")
for i in range(n):
    a, b = list(map(int, input().split()))
    if b > m:
        joy = a - (b - m)
    else:
        joy = a
    f = max(joy, f)
print(f)
