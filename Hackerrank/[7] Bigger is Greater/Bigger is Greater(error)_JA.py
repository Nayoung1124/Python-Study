#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
   # W = list(map(str,w))
    #print(W)
    w_list = list(w)
    pre_list = list(w)
    #print('정렬전',w_list)
    w_list.sort()
    pre_list.sort()
   # print('정렬후',w_list)
    n = len(w_list)
    for i in range(n):
        for j in range(n):
            w_list.insert(i,w_list[j])
            w_list.pop(i+1)
            result = ''.join(w_list)
            if result > w :
               # print ('정답 '+ result)
               return(result)
            else :
                if result == w:
                    return('no answer')
                   # print('no answer '+ result)
                else : 
                    w_list = pre_list
                   # print('다시 '+ result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
