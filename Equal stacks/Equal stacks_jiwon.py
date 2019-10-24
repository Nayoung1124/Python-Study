#!/bin/python3

import os
import sys


# sum_h_list의 모든 요소가 같은 값인지 확인하는 함수
def check_equal(sum_h_list):
    # "sum_h_list의 요소개수"와 "첫번째 요소 값과 같은 값의 개수"가 동일한지 비교
    if len(sum_h_list) == sum_h_list.count(sum_h_list[0]):
        return True
    return False


def equalStacks(h1, h2, h3):
    
    h_list = [h1, h2, h3]
    sum_h_list = [sum(h1), sum(h2), sum(h3)]

    # while문 탈출조건 : sum_h_list의 모든 요소 값이 같아야 함.
    while not check_equal(sum_h_list):
        minimum = min(sum_h_list)
        
        # 최소값(minimum)보다 합이 큰 리스트는 가장 바깥 값 제거
        #                                   & sum_h_list 값 update
        for i in range(3):
            if sum_h_list[i] > minimum:
                x = h_list[i].pop(0)
                sum_h_list[i] -= x

    return sum_h_list[0]

    

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

    fptr.write(str(result))

    fptr.close()
