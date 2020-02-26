#!/bin/python3

import os


def pickingNumbers(a):
    a = sorted(a)
    
    if len(set(a)) == 1:
        return len(a)

    result = a.count(a[0])
    for i in range(1, len(a)):
        result = max(result, a.count(a[i]))
        if a[i] - a[i-1] == 1:
            result = max( result , a.count(a[i])+a.count(a[i-1]) )
   
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result))
    fptr.close()

