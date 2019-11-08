def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i:i+k]
        
        # 문자열 목표 단축길이 (t -> u) : while문 탈출조건에 사용
        u_len = len(set(t)) 

        u, idx = t[0], 1
        while len(u) != u_len:
            u += t[idx] if not t[idx] in t[:idx] else ''
            idx += 1
        print(u)

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
