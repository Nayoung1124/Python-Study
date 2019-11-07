def minion_game(string):
    Vowels = ['A', 'E', 'I', 'O', 'U']
    Stuart, Kevin = 0, 0

    for i in range(len(string)):
        if not string[i] in Vowels:
            Stuart += len(string) - i
        else:
            Kevin += len(string) - i

    if Stuart > Kevin:
        print('Stuart', Stuart)
    elif Stuart < Kevin:
        print('Kevin', Kevin)
    else:
        print('Draw')
            

if __name__ == '__main__':
    s = input()
    minion_game(s)
