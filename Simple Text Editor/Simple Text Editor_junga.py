# Enter your code here. Read input from STDIN. Print output to STDOUT

stack = list()
S = "" 

#S 문자형 변수로 각 코드 연산을 한후에 바로바로 stack 리스트에 넣어줌, 즉, 모든 연산의 값이 저장됨
#이렇게 하면, 되돌아가기 할때 stack의 마지막 자리만 없애서 출력가능

for _ in range(int(input())):
    Q = input().strip().split()
    if Q[0] == '1': #추가
        stack.append(S) #문자형 변수값을 리스트에 추가.
        #print('stack1 =',stack)
        S += Q[1] #Q[1]를 S 문자형에 추가.
      #  print('s1 =',S)
     
    elif Q[0] == '2': #삭제
        stack.append(S)
      #  print('stack2 = ', stack)
        k = int(Q[1]) #숫자형으로 k에 저장해야하므로, 다음과 같이 int형으로 Q 바꿔줌
        S = S[:-k]
       # print('s2 =', S)

    elif Q[0] == '3': #출력
        i = int(Q[1]) - 1 #자리수는 0부터 시작하므로 다음과 같이 쓴다.
        print(S[i])
    else:   
        if len(stack) != 0: #0이 아니면 맨뒤의 값 삭제
            S = stack.pop()
            #print('s4 =',S)
