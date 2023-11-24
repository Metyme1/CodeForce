from collections import Counter

t = int(input())

for _ in range(t):
    s = input()
    button_counts = Counter(s)

    res = ""
    for c in sorted(button_counts):
        if button_counts[c] % 2 != 0:
            res += c

    print(res)
