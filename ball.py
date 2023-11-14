n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

pairs = 0
boy_index = 0
girl_index = 0

while boy_index < n and girl_index < m:
    if abs(boys[boy_index] - girls[girl_index]) <= 1:
        pairs += 1
        boy_index += 1
        girl_index += 1
    elif boys[boy_index] < girls[girl_index]:
        boy_index += 1
    else:
        girl_index += 1

print(pairs)