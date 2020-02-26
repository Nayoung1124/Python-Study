q = int(input())

for q_itr in range(q):
    xyz = input().split()
    a = int(xyz[0])
    b = int(xyz[1])
    c = int(xyz[2])

    if abs(a-c) == abs(b-c):
        print("Mouse C")
    elif abs(a-c) > abs(b-c):
        print("Cat B")
    elif abs(a-c) < abs(b-c):
        print("Cat A")
