#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    S = set(s)
    ans = []

    sw  = s[::-1]
    first = len(s) - len(S)


    for j in range(2,len(s)+1):
        for i in range(len(s)-j+1):
       
            a = s[i:i+j]
            if a in sw:
                b = a[::-1]
                w = [a, b]
                ans.append(w)

            else:
                pass
    print(ans)
    for i in range(len(s)/2):#2씩 증가
        if ans[i][0] = ans[i][1]:
            remove(ans[i])
    
    
    
    
   
    

 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
