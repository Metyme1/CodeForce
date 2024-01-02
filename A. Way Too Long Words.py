n = int(input())
for i in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        wordlen = len(word)
        final = word[0] + str(len(word) - 2) + word[-1]
        print(final)
