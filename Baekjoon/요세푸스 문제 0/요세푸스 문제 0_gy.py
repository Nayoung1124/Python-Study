#'런타임 오류'로 통과되지 않은 코드입니다. 
#hackerrank를 통해 기본 값 7 3 이 주어졌을때 <3, 6, 2, 7, 5, 1, 4>로 출력되는 것을 확인했습니다.

N, K = map(int, input().split()) 
circle = [i for i in range(1, N+1)] 
ans = []

for _ in range(N-1):
    circle += circle[:K-1]
    del circle[:K-1]
    
    ans.append(circle.pop(0))
    
    P = ans + circle
    
print('<', end ='')
print(*P, sep = ', ', end ='>')

