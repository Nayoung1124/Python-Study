
import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input_func().split())
    
    # arr = ['1', '2', ... , 'N']
    arr = list(map(str, range(1, N+1)))   
    
    # 결과 저장할 리스트 선언
    result = []                           
    
    # arr의 요소들이 모두 pop 되어 비어있게 될 때 while문 탈출.
    while len(arr) != 0:
        
        # 맨 앞 숫자를 맨 뒤로 이동 (K-1번 반복)
        for i in range(K-1):        
            arr.append(arr.pop(0))
        
        # 맨 앞 숫자 제거 & 제거된 숫자 result에 저장
        result.append(arr.pop(0))   
    
    
    print('<{}>'.format(', '.join(result)))
