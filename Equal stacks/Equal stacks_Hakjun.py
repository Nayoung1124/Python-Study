#!/bin/python3

import os
import sys
def mk_sum_list(lis):
    result = [0]
    for i in lis[::-1]:
        result.append(result[-1]+i)
    return set(result)

def equalStacks(h1, h2, h3):
    sum1 = mk_sum_list(h1)
    sum2 = mk_sum_list(h2)
    sum3 = mk_sum_list(h3)
    result = sum1 & sum2 & sum3
    return max(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    '''
    #!/bin/python3

    import sys


    n1, n2, n3= input().strip().split(' ')
    n1, n2, n3= [int(n1), int(n2), int(n3)]
    h1=[int(h1_temp) for h1_temp in input(). strip(). split(' ')]
    h2=[int(h2_temp) for h2_temp in input(). strip(). split(' ')]
    h3=[int(h3_temp) for h3_temp in input(). strip(). split(' ')]
    sum1=sum(h1)
    sum2=sum(h2)
    sum3=sum(h3)
    check=sum1==sum2==sum3

    while not check:
        if sum1>=sum2 and sum1>=sum3:
            sum1-=h1.pop(0)
        elif sum2>=sum1 and sum2>=sum3:
            sum2-=h2.pop(0)
        elif sum3>=sum1 and sum3>=sum2:
            sum3-=h3.pop(0)
        check = sum1==sum2==sum3
    print(sum1) 
    '''
