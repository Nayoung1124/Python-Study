import math
import os
import random
import re
import sys
from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
def designerPdfViewer(h, word):
    val=dict(zip(alpha_list, h))
    hh=[]

    for i in word:
        hh.append(val[i])
    
    return max(hh)*len(word)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
