import os

def countingValleys(n, s):
    sum_ = 0 # sum_는 U,D 단계의 합. 이때 sum_ = 0 이면 해수면이다.
    valleys = 0 # 계곡 수

    for i in s:
        if i == 'U':
            sum_ += 1
            if sum_ == 0:
                valleys += 1

        else:
            sum_ -= 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
