n = int(input())
cards = list(map(int, input().split()))
ser = 0
dima = 0
l = 0
r = n - 1
tur = 0

while l <= r:
    if tur == 0:
        if cards[l] > cards[r]:
            ser += cards[l]
            l += 1
        else:
            ser += cards[r]
            r -= 1
    else:
        if cards[l] > cards[r]:
            dima += cards[l]
            l += 1
        else:
            dima += cards[r]
            r -= 1
    tur = 1 - tur
