n = int(input())
students = list(map(int, input().split()))
students = sorted(students)
l = 0
r = 1
tot = 0
while r < n:
    tot += students[r] - students[l]
    l += 2
    r += 2
print(tot)
