n = int(input())
for i in range(n):
    m = int(input())
    s = input()
    if sorted(s) != sorted("Timru"):
        print("NO")
        continue
    print("YES")
