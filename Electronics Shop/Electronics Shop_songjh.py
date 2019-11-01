import os

sum_list = [] # 키보드+USB 의 모든 경우의 값을 저장하는 리스트
over_list = [] # 예산을 초과하는 키보드+USB 의 값을 저장하는 리스트
max_vals = [0] # 출력하기 위한 리스트

def getMoneySpent(keyboards, drives, b):
    for i in range(n):
        for j in range(m):
            val = keyboards[i] + drives[j]
            sum_list.append(val)

            if val <= b :
                if val >= max_vals[-1] :
                    max_vals.append(val)
                    # append는 왼쪽에서 오른쪽으로 쌓이므로 
                    # 결국 max_vals 리스트의 마지막 요소의 값은 val의 최댓값이 된다.

            else :
                over_list.append(val)
                if len(sum_list) == len(over_list) :
                    max_vals.append(-1)
                    
    return max_vals[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
