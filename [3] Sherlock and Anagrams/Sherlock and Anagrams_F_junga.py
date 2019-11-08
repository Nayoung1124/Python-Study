#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    l_s = list(s) #l_s에 s를 리스트 형식으로 저장
    l__s= []
    n_ls = len(l_s)
    count = 0

    for i in range(1 << n_ls):
         for j in range(n_ls):
                if (i & (1 << j)): # 부분집합 만들어줌
                    l__s.append(l_s[j])
                    print(l__s)
                    if sorted(l__s[n_ls : j]) == l__s:
                        count += 1

    return count



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
