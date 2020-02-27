import sys
input_func = sys.stdin.readline


# 재귀함수
def Quad_Tree(N, Map):
    
    # 재귀함수 탈출조건: 현재 입력으로 들어온 Map의 길이가 0인 경우
    if len(Map) == 0:
        return
    
    # 현재 입력으로 들어온 Map의 요소들이 모두 1인경우 '1' 반환
    if '0' not in sum(Map, []):
        return '1'
    
    # 현재 입력으로 들어온 Map의 요소들이 모두 0인경우 '0' 반환
    elif '1' not in sum(Map, []):
        return '0'
    
    # 그 외의 경우 Map을 4분할하여 Quad_Tree함수 다시 호출
    string = '({}{}{}{})'.format(
        Quad_Tree(N//2, [x[:N//2] for x in Map[:N//2]]),
        Quad_Tree(N//2, [x[N//2:] for x in Map[:N//2]]),
        Quad_Tree(N//2, [x[:N//2] for x in Map[N//2:]]),
        Quad_Tree(N//2, [x[N//2:] for x in Map[N//2:]])
    )
    return string


if __name__ == '__main__':
    N = int(input_func())
    Map = [list(input_func().strip()) for _ in range(N)]
    string = Quad_Tree(N=N, Map=Map)
    print(string)
