#!/bin/python3

import os


def dynamicArray(n, queries):
    result = []
    # n개의 sequence 들을 포함한 리스트 생성
    seqList = [list() for _ in range(n)]

    # lastAnswer 초기화
    lastAnswer = 0

    for q_type, x, y in queries:
        if q_type == 1:
            seq_idx = (x ^ lastAnswer) % n
            seqList[seq_idx].append(y)

        elif q_type == 2:
            seq_idx = (x ^ lastAnswer) % n
            element_idx = y % len(seqList[seq_idx])
            lastAnswer = seqList[seq_idx][element_idx]
            # print(lastAnswer)
            result.append(lastAnswer)

    return result
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
