#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the gridSearch function below.
def gridSearch(G, P):
    
    p=len(P)

    a = 0
    b = []#해당하는 문자열이 있는 문제 문자열 저장
    d=[] #
    for i in G:
        for j in range(len(P)):
            if i.find(P[j]) >= 0:
                for k in re.finditer(P[j],i):
                    d.append(k.start())
                    continue
                d.append('***')
                # c.append(i)
                b.append(i.find(P[j]))
                a += 1

    if a == len(P):
        aa = [[] for i in range(len(P))]
        bb=[]
        j = 0
        for i in d:
            if i != '***':
                aa[j].append(i)
            else:
                j += 1
        # return(aa)
        for i in range (len(aa)):
            if i != len(aa)-1:
                bb.append(list(set(aa[i]).intersection(aa[i+1])))
            else:
                pass
        return('YES')
    else:
        return ('NO')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
    
    
    
#aa = [[0, 2, 4], [4]]
#     [[4]]
