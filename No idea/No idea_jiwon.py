# Enter your code here. Read input from STDIN. Print output to STDOUT

def NoIdea(A, B, array):
    happiness = 0
    for x in array:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
    return happiness


if __name__ == '__main__':
    n, m = input().strip().split(' ')
    array = input().strip().split(' ')
    A = set(input().strip().split(' '))
    B = set(input().strip().split(' '))

    happiness = NoIdea(A, B, array)

    print(happiness)
