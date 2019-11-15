import os

sum_number = []

def pickingNumbers(a):
    a.sort() # 오름차순 정렬
    for i in range(n-1):
        num_list = []
        num_list.append(a[i])
        for j in range(n):
            if i < j:
                if num_list[0] == a[j] or num_list[0] == a[j]-1:
                    num_list.append(a[j])
        sum_number.append(len(num_list))
    
    if len(sum_number) == 1:
        return sum_number[0]
    else:
        return max(sum_number)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
