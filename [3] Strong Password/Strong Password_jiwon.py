#!/bin/python3

import os


def minimumNumber(n, password):

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    flag = {'num': False, 'lower': False, 'upper': False, 'special': False}
    password = list(set(password))

    for x in password:
        if (not flag['num']) and (x in numbers):
            flag['num'] = True
        elif (not flag['lower']) and (x in lower_case):
            flag['lower'] = True
        elif (not flag['upper']) and (x in upper_case):
            flag['upper'] = True
        elif (not flag['special']) and (x in special_characters):
            flag['special'] = True
    
    count_False = list(flag.values()).count(False)
    
    # Ab1  --> 6 - n = 3 출력
    # 4700 --> count_False = 3 출력
    if n < 6:
        return max(6 - n, count_False)

    return count_False
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer))
    fptr.close()
