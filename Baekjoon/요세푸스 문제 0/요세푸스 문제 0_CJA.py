import sys
N, M = list(map(int,sys.stdin.readline().split()))
list_ = [] #1~N까지의 수를 담는 리스트
res = []  #M 건너뛰고 삭제한 수를 담는 리스트
cnt = M -1 #삭제할 인덱스를 계산하기 위한 변수

for i in range(N): # 1~N까지의 수를 만들어서 리스트에 저장
    list_.append(i+1)

for _ in range(N-1):
    #print(cnt)
    res.append(list_.pop(cnt)) # M번째 삭제
    cur = cnt -1 #삭제하는 순간 인덱스는 하나둘어든다(M번째가 삭제되었으니 당연히 커서(?)가 하나 줄어든다.)

    temp = cur + M #인덱스에 M을 더한다.
    temp_ = len(list_) #삭제후 리스트의 길이 반환 (이유)리스트보다 temp가 더 크면 안된다 따라서 이를 비교하기 위함으로

    if temp < temp_: # 만약temp_가 더 크면 
        cnt = temp

    else: #만약 temp_가 더 작으면 temp_가 더 커질때까지 나눈다.
        cnt = temp % temp_

res.append(list_.pop())   
res = map(str,res)

print('<'+', '.join(res)+'>')
