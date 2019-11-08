# Enter your code here. Read input from STDIN. Print output to STDOUT

def n_P_k(n, k):
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    return result


def n_C_k(n, k):
    # 10_C_3 =  n_P_k / k! = (10 * 9 * 8) / (3 * 2 * 1)
    
    if k > n:
        return 0

    # 10_C_7 = 10_C_3
    k = min(n-k, k)

    return n_P_k(n, k) / n_P_k(k, k)

    
def calculate_prob(n, k, array):
    # 전체 조합 개수
    total_combination = n_C_k(n, k)

    # a를 포함하는 조합 개수 = (전체 조합 개수) - (a를 포함하지 않는 조합 개수)
    num_not_a = len(array) - array.count('a')
    a_combination = total_combination - n_C_k(num_not_a, k)

    return a_combination / total_combination



if __name__ == '__main__':
    n = int(input().strip())
    array = input().strip().split(' ')
    k = int(input().strip())

    answer = calculate_prob(n, k, array)
    print(answer)
