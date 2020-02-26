def minion_game(s):
    # your code goes here
    Stuart = 0
    Kevin = 0
    A = len(s)
    for i in range(A):
        if s[i] in ['A', 'E', 'I', 'O', 'U']:
            Kevin += A - i
        else:
            Stuart += A - i

    if Kevin > Stuart:
        print('Kevin', Kevin)
    elif Kevin < Stuart:
        print('Stuart', Stuart)
    else:
        print('Draw')


if __name__ == '__main__':