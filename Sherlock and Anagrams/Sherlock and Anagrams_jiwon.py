#!/bin/python3

import os
import sys

def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)):
        temp_list = [''.join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        # ex) i=1, s='cdcd' --> temp_list: ['c', 'd', 'c', 'd']
        # ex) i=2, s='cdcd' --> temp_list: ['cd', 'cd', 'cd']
        # ex) i=3, s='cdcd' --> temp_list: ['ccd', 'cdd']
        
        # 중복이 0개일 경우 바로 다음 i번으로
        if len(set(temp_list)) == len(temp_list):
            continue
        else:
            for i, x in enumerate(temp_list):
                count += temp_list[i+1:].count(x)
    
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
