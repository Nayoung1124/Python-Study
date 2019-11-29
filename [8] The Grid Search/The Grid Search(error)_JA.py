def gridSearch(G, P):
    R = len(G) #10
    C = len(G[0]) #10
    r = len(P) #3
    c = len(P[0]) #4
    count = 0
    G_ = ''

    for i in range(R):
        G_ += G[i]
    for n in range(r):
        for m in range(len(G_)-c+1):
            #print (P[n])
            #print (G_[m:m+c])
            #print("---")
            
            if G_[m:m+c] == P[n]:
                print (P[n])
                count +=1
                if count == r:
                    return "YES"
                else :
                    return "NO"
