#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    E_word = 'abcdefghijklmnopqrstuvwxyz'
    l =[]
    for i in range(len(word)):
        for j in E_word:
            if word[i] == j:
                num_ = E_word.index(j)
                l.append(h[num_])
                
    l_max = max(l)
    result = l_max * len(word)
    return (result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
