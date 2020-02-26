import os
# import re

def gridSearch(G, P):  
    for G_idx, G_line in enumerate(G):
        ''' check num of lines '''
        if len(G)-G_idx < len(P):
            return 'NO'
        
        ''' search the first line of P '''
        f_count = G_line.count(P[0])
        if f_count == 0:
            continue
        # tmp_cols = [s.start() for s in re.finditer(P[0], G_line)] --> '1111111111'에서 '11111'의 위치들을 다 못찾음.
        tmp_cols = [c for c in range(len(G_line)) if G_line.startswith(P[0], c)]

        ''' check the rest of the lines of P '''
        for col in tmp_cols:
            for P_idx, P_line in enumerate(P):
                if P == 0: continue

                if G[G_idx+P_idx][col:col+len(P_line)] == P_line: pass
                else: break
            else:
                return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()
