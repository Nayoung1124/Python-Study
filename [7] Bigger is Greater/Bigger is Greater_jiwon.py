
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

    
    
    
    
    


    
# ------------------------------------------------------------------
# Code Description
# ------------------------------------------------------------------

import os


def str2str_sorted(s):
    # Alphabetically Order
    return ''.join(sorted(list(s)))

def str2str_reverse(s):
    # Alphabetically Reverse Order
    return ''.join(sorted(list(s), reverse=True))

def get_bigger_str(s):
    # 3) s='dkhc' ( = '2431' )
    for i in range(len(s) - 1, 0, -1):
        if s[i - 1] > s[i]:
            # 4)  i=3 --> 3(h) > 1(c) --> True
            #     i=2 --> 4(k) > 3(h) --> True
            #     i=1 --> 2(d) > 4(k) --> False
            continue
        # 5) i=1 -->  s[i-1]=2(d)  s[i:]=431(khc)
        tmp = str2str_sorted(s[i:])
        # 6) s[i:]='khc' --> tmp='chk'(134)
        for j in range(len(tmp)):
            if s[i - 1] < tmp[j]:
                # 7)          s[i-1]   tmp[j]
                #     j=0 -->  2(d)  >  1(c) --> False
                #     j=1 -->  2(d)  >  3(h) --> True
                return tmp[j] + tmp[:j] + s[i - 1] + tmp[j + 1:]
                # 8)     3(h)     1(c)       2(d)        4(k)       ==> hcdk


def biggerIsGreater(w):
    # 1) w = 'adkhc'
    if w == str2str_reverse(w):
        # ex) w='cba'
        return 'no answer'

    for i in range(len(w)-2, -1, -1):
        tmp = w[i:]
        # 2) i=3 --> tmp='hc'  /  i=2 --> tmp='khc'  /  i=1 --> tmp='dkhc'
        if tmp == str2str_reverse(tmp):
            continue

        bigger_str = get_bigger_str(tmp)
        # 9) tmp='dkhc' --> bigger_str='hcdk'

        return w[:i] + bigger_str
        # 10)    'a'  +  'hcdk'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()



