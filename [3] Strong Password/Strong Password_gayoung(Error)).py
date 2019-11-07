#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    if n < 7:
        print(n)
        return n
        sys.exit(1)

    A = set(string.ascii_uppercase)
    a = set(string.ascii_lowercase)
    num = set(string.digits)
    spec = set(string.punctuation)

    count = 0


    if not A.intersection(password):
        count += 1
    if not a.intersection(password):
        count += 1
    if not num.intersection(password):
        count += 1
    if not spec.intersection(password):
        count += 1
        print("비었다")
    
    print(count)
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    S = input()
    password = set(S)
    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
