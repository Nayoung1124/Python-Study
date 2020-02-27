X = int(input())
count = 0
result = [X]
def calculation(x):
    a = []
    for i in x:
        a.append(i-1)
        if i%3 ==0:
            a.append(i/3)
        if i%2 ==0:
            a.append(i/2)
    a = set(a)
    a = list(a)
    return a
while True:
    if X == 1:
        break
    temp = result
    result = []
    result = calculation(temp)
    count += 1
    if min(result) == 1:
        break
print(count)
