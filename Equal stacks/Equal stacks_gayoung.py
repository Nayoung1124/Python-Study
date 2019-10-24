#!/bin/python3

import os
import sys


def removeTOP(value):
    print("remove함수 실행됨")

    top = max(value)
    print("가장 큰 값", top)

    arr = value.index(top)
    print(arr, "요게 arr. 아마도 top의 인덱스 도출")

    if arr == 0:
        h1.pop(0)
    elif arr == 1:
        h2.pop(0)
    elif arr == 2:
        h3.pop(0)

    print("수정된 h들")
    print(h1, h2, h3)

    return [h1, h2, h3]


# 합을 계속 해주어야 한다는 계산량 문제가 있음

def equalStacks(h1, h2, h3):
    a = sum(h1)
    b = sum(h2)
    c = sum(h3)
    result = 0
    value = [a, b, c]
    print(value, "총 합계")
    print("result", result)
    if a == b == c:
        print("result a 나와야 하는 경우")
        result = a
        print(result)
        return result



    else:
        print("removetop 실행되는 경우")
        revised = removeTOP(value)
    print("안나와야 나와야 하는 문장")
    return equalStacks(*revised)


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
    print(result, "출력단 result")
    fptr.write(str(result) + '\n')

    fptr.close()
