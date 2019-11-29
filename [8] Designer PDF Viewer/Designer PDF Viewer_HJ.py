#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    a = string.ascii_lowercase
    words = set(word)
    temp = []
    m = -1

    for i in words:
        temp.append(a.find(i))
    
    for i in temp:
        m = max([m, h[i]])
    
    return m*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
