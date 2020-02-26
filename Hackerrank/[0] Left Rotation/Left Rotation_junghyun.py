if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0]) # a리스트의 요소 수 1~
    d = int(nd[1]) # 회전시킬 수
    a = list(map(int, input().rstrip().split())) #맨 처음의 리스트

    result = a[d:] + a[:d]
    # result는 a 리스트의 d번째부터 d미만번째까지의 요소가 더 해져있다.

    print (*result) # 리스트 요소 출력
