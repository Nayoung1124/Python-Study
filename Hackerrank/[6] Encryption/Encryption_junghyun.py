import math
import os

list_s = []
num = []
list_num = []

def encryption(s):
    list_s = list(s) # 문자열을 리스트로 변환
    L = len(list_s) # 문자열 길이
    L_root = math.sqrt(L) #루트
    low = math.floor(L_root) # 내림
    high = math.ceil(L_root) # 올림

    for i in range(low,high+1):
        num.append(i) # low와 high 사이의 값들을 num 리스트 저장
    
    for x in range(len(num)):
        for y in range(len(num)):
            if num[x] <= num[y] and num[x]*num[y] >= L:
                list_num.append(num[x]) # 행:row (list_num[0]만 사용)
                list_num.append(num[y]) # 열:column (list_num[1]만 사용)

    result = "" # 문자열로 결과를 출력하기 위해
    n = 0
    for i in range(n, list_num[1], 1):
        result += s[n::list_num[1]] + " "  # n부터 끝까지 list_num[1] 간격으로
        n += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
