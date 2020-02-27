import sys

input_func = sys.stdin.readline

if __name__ == '__main__':
    # N을 입력받아 그 크기만큼 DP_arr 리스트를 미리 선언 (DP_arr에는 "해당 값(index 값)에 도달하기까지의 연산 횟수"를 저장)
    N = int(input_func())
    DP_arr = [0] * (N + 1)  

    # 1부터 N-1까지 돌면서 DP_arr 채우기
    for i in range(1, N):
        # i+1 값이 N 이하이면서, DP_arr[i+1]의 값이 존재하지 않거나 현재 DP_arr[i+1]에 저장된 값이 DP_arr[i] + 1 값(현재 연산횟수+1)보다 큰 경우에만 update.
        if (i + 1 <= N) and (DP_arr[i + 1] == 0 or DP_arr[i + 1] > DP_arr[i] + 1):
            DP_arr[i + 1] = DP_arr[i] + 1
        
        # i*2 값이 N 이하이면서, DP_arr[i*2]의 값이 존재하지 않거나 현재 DP_arr[i*2]에 저장된 값이 DP_arr[i] + 1 값보다 큰 경우에만 update.
        if (i * 2 <= N) and (DP_arr[i * 2] == 0 or DP_arr[i * 2] > DP_arr[i] + 1):
            DP_arr[i * 2] = DP_arr[i] + 1
        
        # i*3 값이 N 이하이면서, DP_arr[i*3]의 값이 존재하지 않거나 현재 DP_arr[i*3]에 저장된 값이 DP_arr[i] + 1 값보다 큰 경우에만 update.
        if (i * 3 <= N) and (DP_arr[i * 3] == 0 or DP_arr[i * 3] > DP_arr[i] + 1):
            DP_arr[i * 3] = DP_arr[i] + 1

    print(DP_arr[N])



    """ (예시 - N=10인 경우)
                             1  2  3  4  5  6  7  8  9  10
                i = 1 -> [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
                i = 2 -> [0, 0, 1, 1, 2, 0, 2, 0, 0, 0, 0]
                i = 3 -> [0, 0, 1, 1, 2, 0, 2, 0, 0, 2, 0]
                i = 4 -> [0, 0, 1, 1, 2, 3, 2, 0, 3, 2, 0]
                i = 5 -> [0, 0, 1, 1, 2, 3, 2, 0, 3, 2, 4]
                i = 6 -> [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 4]
                i = 7 -> [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 4]
                i = 8 -> [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 4]
                i = 9 -> [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
          출력 : DP[10] = 3
    """

