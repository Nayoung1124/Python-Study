import os
from string import ascii_lowercase


def designerPdfViewer(h, word):
    alphabet = list(ascii_lowercase)
    h_dict = dict(zip(alphabet, h))
    word_h = list(map(lambda s: h_dict[s], word))
    return max(word_h) * len(word_h)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result))
    fptr.close()
