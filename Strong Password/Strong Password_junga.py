#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.

def minimumNumber(n, password):
    n_count = 0
    l_count = 0
    u_count = 0
    s_count = 0
    number = False
    lower = False
    upper = False
    special = False
    for i in password:
        if not number and i.isdigit(): #숫자
            n_count += 1
            number = True
        if not lower and i.islower(): #소문자
            l_count += 1
            lower = True
        if not upper and i.isupper(): #대문자
            u_count += 1
            upper = True
        if not special and i in "!@#$%^&*()-+": #특수문자
            s_count += 1
            special = True

        count = n_count + l_count + u_count + s_count


    if len(password) >= 6 : 
        #result.append(4-count)
        return 4-count
    elif len(password) - count <= 1:
        
        if 6-len(password) < 4 - count:
            return 4 - count
        
        else:
            return 6 - len(password)

    else:
        return 4 - count 




    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
