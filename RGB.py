n = int(input())
s = list(input())
a = 0
b = 1
arr1 = []
while b < len(s):
    if s[a] != s[b]:
        arr1.append(s[a])
        a += 1
        b += 1
    else:
        a += 1
        b += 1
print(n - len(arr1) - 1)
