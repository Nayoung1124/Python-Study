#'틀렸습니다' _ 통과안된 코드입니다. 기본코드는 hackerrank에서 틀리지 않게 돌아가는 것을 확인했습니다.

X = int(input())
ans = [0,1,1,1]

for i in range(4,X+1):
    
    sum_list = []

    if i % 3 == 0:
        c = i//3
        count_c = ans[c] + 1
        sum_list.append(count_c)
    

    if i % 2 == 0:
        a = i//2
        count_a = ans[a] + 1
        sum_list.append(count_a)

    b = i-1
    count_b = ans[b] + 1
    sum_list.append(count_b)
    answer = min(sum_list)
    ans.append(answer)
    
print(ans[X])
