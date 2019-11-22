
import os


def str2str_sorted(s):
    return ''.join(sorted(list(s)))

def str2str_reverse(s):
    return ''.join(sorted(list(s), reverse=True))

def get_bigger_str(s):
    for i in range(len(s)-1, 0, -1):
        if s[i-1] > s[i]:
            continue
        tmp = str2str_sorted(s[i:])
        for j, t in enumerate(tmp):
            if s[i-1] < t:
                return tmp[j] + tmp[:j] + s[i-1] + tmp[j+1:]

def biggerIsGreater(w):
    if w == str2str_reverse(w):
        return 'no answer'
    for i in range(len(w)-2, -1, -1):
        tmp = w[i:]
        if tmp == str2str_reverse(tmp):
            continue
        bigger_str = get_bigger_str(tmp)
        return w[:i] + bigger_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()


