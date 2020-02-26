#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    for idx, i in enumerate(G):
        A = i.find(P[0])
        while A != -1:
            if len(G)-idx < len(P): break
            for idx2, j in enumerate(P):
                B = G[idx+idx2].find(j, A)
                if B == -1 or A != B: break
                if idx2 == len(P)-1:
                    return 'YES'
            A = i.find(P[0], A+1)
    return 'NO'

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
