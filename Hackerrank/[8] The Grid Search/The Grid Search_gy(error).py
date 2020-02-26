#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    R = len(G[0])
    r = len(P[0])
    #print(R)
    #print(r)
    #print(R-r+1)
    #print(len(P))
    #print(P)
    #print(G[0][:r])
    yes = []
    for h in range(R-r+1):
        
        for i in range(len(G)-3):
            line = G[i][h:h+r]
            count = 0
            
            #print(line)
            #print(P[0])

            if line == P[0]:
                #print(P[0])
                #print("있기는 함")
                
                #print(count)
                for j in range(len(P)):
                    #print(P[j])
                    line_ = int(line)
                    pp = int(P[j])
                    print(line_,pp)
                    if line_ == pp:
                        #print(pp)
                        #print("yes")
                        #print(P[j])
                        count = count + 1
                        #print(count)
                        #yes.append(P[j]) 
                    print(count)
                if count == len(P):
                    #print(count)
                    #print(len(P))
                    return 'YES'
            else:
                continue
            ##print(count)
        #print("한칸밀림")
    #print(count)
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
