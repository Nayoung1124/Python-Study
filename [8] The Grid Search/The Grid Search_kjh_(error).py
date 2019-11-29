(1) 8/16 test cases failed :(


import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    # G = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137'
    # P = ['9505', '3845', '3530']
    YES=[]

    for i in range(r):
        for j in range(R):
            if P[i] in G[j]:
                YES.append(i)
               
    if len(YES)==len(P):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0]) #10

        C = int(RC[1]) #10

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0]) #3

        c = int(rc[1]) #4

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
