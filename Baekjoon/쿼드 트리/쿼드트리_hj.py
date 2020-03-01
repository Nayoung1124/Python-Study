from itertools import chain
import sys
input = sys.stdin.readline

def func(n, image):
    if not '0' in list(chain(*image)): return '1'
    if not '1' in list(chain(*image)): return '0'
    result ='('
    n = n//2
    result += func(n, [i[:n] for i in image[:n]])
    result += func(n, [i[n:] for i in image[:n]])
    result += func(n, [i[:n] for i in image[n:]])
    result += func(n, [i[n:] for i in image[n:]])
    result += ')'
    return result

N = int(input())
image = [input().strip() for _ in range(N)]
print(func(N, image))