#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    height = []
    alpha_list = list(ascii_lowercase) #a~z까지 리스트에 불러옴
    
    for i in word: # 'abc'에서 하나씩 가져옴
        finder = alpha_list.index(i) #ex.'c'가 알파벳리스트에서 어떤 인덱스(위치)에 있는지 
        height.append(h[finder]) # h리스트에서 찾아 놓은 인덱스 값을 가져옴(매칭)
    width = max(height) #가져온 height중 가장 큰거 (=세로)
    length = len(word) #문자열 길이(=가로)

    return width * length #면적



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
