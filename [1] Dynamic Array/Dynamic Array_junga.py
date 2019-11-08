
import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    s0 = []
    s1 = []
    #last_ = 0
    last_ = [0]
    for i in range(q):
        if queries[i][0] == 1:
            if (queries[i][1]^last_[-1])%2 == 0:
                s0.append(queries[i][2])
            else :
                s1.append(queries[i][2])
               
        else:
            if (queries[i][1]^last_[-1])%2 == 0:
                #last_ = s0[-1]
                last_.append(s0[-1])
                
            else :
               # last_ = s1[-1]
                last_.append(s1[-1])
                

    
    return(last_[1:])
                    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
   

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
