import os

def equalStacks(h1, h2, h3):
    H1 = sum(h1)
    H2 = sum(h2)
    H3 = sum(h3)
    least = min(H1, H2, H3)
    most = max(H1, H2, H3)

    while most > least:
        if most == H1:
            H1 -= h1.pop(0)
        elif most == H2:
            H2 -= h2.pop(0)
        else:
            H3 -= h3.pop(0)
        least = min(H1, H2, H3)
        most = max(H1, H2, H3)
    return most

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
