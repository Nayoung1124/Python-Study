#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    n_txt = []
    m_txt = []
    txt = list(word)
    for i in txt:
        n_txt.append(ord(i)-96)
    print(n_txt)

    for i in range (len(n_txt)):
        n_txt[i]=h[n_txt[i]-1]

    return (len(word)* max(n_txt))
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
