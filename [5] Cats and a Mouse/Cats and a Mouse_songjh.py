import os

def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    if a < b:
        return 'Cat A'

    elif a > b:
        return 'Cat B'
    
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0]) # 고양이1

        y = int(xyz[1]) # 고양이2

        z = int(xyz[2]) # 쥐

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
