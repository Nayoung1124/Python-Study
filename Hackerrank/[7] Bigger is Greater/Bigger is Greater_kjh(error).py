import math
import os
import random
import re
import sys
import itertools

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    ans=''
    k=list(w)
    kk=k
    if k==sorted(k, reverse=True) or len(set(k))==0:
        return "no answer"
    elif k[-2]<k[-1]:
        a=k.pop() #k[-1]
        b=k.pop() #k[-2]
        k.append(a)
        k.append(b)
        ans=''.join(k)
        '''
    elif k[-3]<k[-2]:
        c=k[-3:]
        del k[-3:]
        cc=itertools.permutations(c)
        d=cc.index(c)
        dd=cc[d+1]
        ans=''.join(dd)
        '''
    else:
        z=itertools.permutations(kk)
        y=z.index(kk)
        x=z[y+1]
        ans=''.join(x)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input()) #5

    for T_itr in range(T):
        w = input() #ab, bb, hefg ... 

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
