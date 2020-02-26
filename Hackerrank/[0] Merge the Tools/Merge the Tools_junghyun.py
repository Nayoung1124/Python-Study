from collections import OrderedDict # 문자열 중복 제거 코드
def merge_the_tools(string, k):
    n = len(string)
    out = int(n/k)

    for i in range (out):
        result = string [k*i:k*(i+1)] #문자열 슬라이싱

        print ("".join(OrderedDict.fromkeys(result)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
