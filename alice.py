n = int(input())
m = int(input())

n = sorted(str(n))
l = 0
r = 1
while r < len(n):
    if n[l] == 0:
        n[l], n[r] == n[r], n[l]
        l += 1
    else:
        r += 1
print(n)
