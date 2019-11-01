"47/90 fail"

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    len_password=len(password)
    list_password=list(password)
    score=0

    if len_password < 6:
        a = 6-len_password
        return a
    elif numbers not in list_password:
        score+=1
        return score
    elif lower_case not in list_password:
        score+=1
        return score 
    elif upper_case not in list_password:
        score+=1
        return score
    elif special_characters not in list_password:
        score+=1
        return score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
