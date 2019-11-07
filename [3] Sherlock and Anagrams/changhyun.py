#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(string):
    result = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            for n in range(1, len(string)-j+1):
                if sorted(string[i:i+n]) == sorted(string[j:j+n]):
                    result += 1
 
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
