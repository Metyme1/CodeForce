n = int(input())
count = 0
for i in range(n):
    a, b, c = map(int, input().split())
    count += a + b + c
if count == 0:
    print("YES")
else:
    print("NO")
