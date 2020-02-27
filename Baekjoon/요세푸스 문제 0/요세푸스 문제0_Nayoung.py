import sys
n,k=map(int,sys.stdin.readline().split())
nums=[p for p in range(1,n+1)]
ans=[]
temp=k-1
for i in range(n):
    if len(nums) > temp:
        ans.append(nums.pop(temp))
        temp+=k-1 # temp번째 수가 제거 되었고 (k-1)만큼 다음수가 시작 인덱스가 됨

    elif len(nums) <= temp:
        temp = temp%len(nums)
        ans.append(nums.pop(temp))
        temp += k-1
        
print('<',end='')
for i in ans:
    if i==ans[-1]:print(i,end='')
    else: print("%s, "%(i),end='')
print('>',end='')

