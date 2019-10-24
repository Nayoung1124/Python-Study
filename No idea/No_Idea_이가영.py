n, m = input().split()
whole = list(map(int, input().split()))

score = 0

a = set(map(int, input().split()))
b = set(map(int, input().split()))

for i in whole:

    if i in a:
        score += 1

    if i in b:
        score -= 1

    else:
        pass

print(score)


