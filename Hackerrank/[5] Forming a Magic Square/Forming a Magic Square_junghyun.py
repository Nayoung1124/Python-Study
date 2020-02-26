import os

def formingMagicSquare(s):
    case1=[[2,7,6],[9,5,1],[4,3,8]]
    case2=[[2,9,4],[7,5,3],[6,1,8]]
    case3=[[4,3,8],[9,5,1],[2,7,6]]
    case4=[[4,9,2],[3,5,7],[8,1,6]]
    case5=[[6,7,2],[1,5,9],[8,3,4]]
    case6=[[8,1,6],[3,5,7],[4,9,2]]
    case7=[[8,3,4],[1,5,9],[6,7,2]]
    case8=[[6,1,8],[7,5,3],[2,9,4]]

    cost1=0
    for i in range(3):
        for j in range(3):
            cost1+=abs(s[i][j]-case1[i][j])

    cost2=0
    for i in range(3):
        for j in range(3):
            cost2+=abs(s[i][j]-case2[i][j])

    cost3=0
    for i in range(3):
        for j in range(3):
            cost3+=abs(s[i][j]-case3[i][j])

    cost4=0
    for i in range(3):
        for j in range(3):
            cost4+=abs(s[i][j]-case4[i][j])

    cost5=0
    for i in range(3):
        for j in range(3):
            cost5+=abs(s[i][j]-case5[i][j])

    cost6=0
    for i in range(3):
        for j in range(3):
            cost6+=abs(s[i][j]-case6[i][j])

    cost7=0
    for i in range(3):
        for j in range(3):
            cost7+=abs(s[i][j]-case7[i][j])

    cost8=0
    for i in range(3):
        for j in range(3):
            cost8+=abs(s[i][j]-case8[i][j])

    return min(cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
