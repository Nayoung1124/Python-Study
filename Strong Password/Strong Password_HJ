#!/bin/python3

import math
import os
import random
import re
import sys

numbers = set("0123456789")
lower_case = set("abcdefghijklmnopqrstuvwxyz")
upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = set("!@#$%^&*()-+")

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    result = 0
    temp = set(password)
    if len(temp & numbers) == 0:
        result += 1

    if len(temp & lower_case) == 0:
        result += 1

    if len(temp & upper_case) == 0:
        result += 1

    if len(temp & special_characters) == 0:
        result += 1
    
    if n + result < 6:
        result += 6 - n - result
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
