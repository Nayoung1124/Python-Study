S_stack = []
#S = ""
N = int(input())

for i in range(N):
    n1N2 = input().split()
    n1 = int(n1N2[0])

    if n1 == 1:
        S_stack.append(n1N2[1])

    elif n1 == 2:
        del S_stack [n1N2[1]:-1]
        #S_stack.pop(-1)

    elif n1 == 3:
        print(S_stack[-1][-1])

    else:
        n1N2[1] = S_stack.pop(-1)
