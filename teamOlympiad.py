n = int(input())
teams = list(map(int, input().split()))
math = []
pe = []
Pr = []

for i in range(len(teams)):
    if teams[i] == 1:
        math.append(i + 1)
    elif teams[i] == 2:
        pe.append(i + 1)
    else:
        Pr.append(i + 1)
nums = min(len(math), len(pe), len(Pr))

if nums == 0:
    print(0)
else:
    print(nums)
    for i in range(nums):
        print(math[i], pe[i], Pr[i])
