def merge_the_tools(string, k):
    n = len(string)
    A = k
    for i in range(0, n, A):
        S = string[i:i + A]
        for j in range(len(S)):
            #if subsegment.count(subsegment[j])>1:
                temp_ = sorted(set(S), key=S.index)
                result = ''.join(temp_)
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
