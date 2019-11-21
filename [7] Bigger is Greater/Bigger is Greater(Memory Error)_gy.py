#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = tuple(w)
    W = sorted(w)
    n = len(w)
    Ans = ''
    S = list(permutations(W,n))    
    ind = S.index(w)

    if S[-1] == w:
        return "no answer"
    ans = list(S[ind+1])

    
    for i in range(n):
        Ans += ans[i]

    return Ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
