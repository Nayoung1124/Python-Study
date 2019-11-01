import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    number = 0

    if numbers not in password:
        number += 1

    elif lower_case not in password:
        number += 1

    elif upper_case not in password:
        number += 1

    elif special_characters not in password:
        number += 1

    # 아래쪽은 return 부분
    if len(password) >= 6: 
        return number

    elif 6-len(password) > number:
        return 6-len(password)
        
    elif 6-len(password) < number:
        return number

    else:
        return number 
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
