n, k = map(int, input().split())
n_list = [i for i in range(1, n+1)]
res = []
k_ = k

while len(n_list) != 0:
    if len(n_list) > k_: # n_list 요소의 수가 k_의 수보다 클 경우
        res.append(n_list[k_-1])
        # k번째 요소를 추가하기 위해 n_list의 k_-1 (리스트는 0번째 인덱스부터 존재하므로) 인덱스의 요소를 res 리스트에 apped해준다.
        
        n_list.pop(k_-1) 
        # res에 append했으므로 n_list에서는 삭제한다.
        
        n_list = n_list[k_-1:] + n_list[:k_-1] 
        # 제거 후 남은 요소의 순서를 k_-1 번째 부터로 바꾼다. 예를들어 3을 삭제 후 [1,2,4,5,6,7]이 남았다면 이것을 [4,5,6,7,1,2]의 순서로 변경한다.
        
        k_ = k
        # 세번째 if문에서 k_의 값이 변했을 경우가 있으므로 k_를 다시 k의 값으로 초기화 해준다.

    elif len(n_list) == k_: # n_list 요소의 수와 k_의 수와 같을 경우
        res.append(n_list[-1])
        # ex) k_=3 이고 n_list=[5,1,4]인 경우 마지막 요소를 append한다.
        
        n_list.pop()
        # res에 append했으므로 n_list에서 마지막 요소 삭제한다.
        
        k_ = k
        # 세번째 if문에서 k_의 값이 변했을 경우가 있으므로 k_를 다시 k의 값으로 초기화 해준다

    elif len(n_list) < k_: 
        # ex) k_=3 이고 n_list=[5,1]인 경우 5->1->5의 순서이므로 5를 append해야 하므로 K_의 값을 3에서 3-2=1의 값으로 변경해서 첫번째 if문의 과정을 수행하도록한다.
        k_ = k_ - len(n_list)
        
    elif len(n_list) == 1: # n_list의 요소가 한개만 남았을 경우
        res.append(*n_list)
        n_list.pop()

print('<', end ='')
print(*res, sep = ', ', end ='>')
