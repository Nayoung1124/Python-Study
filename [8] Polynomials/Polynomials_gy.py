import numpy as np

p = list(input().split())
x = int(input())
P = np.array(p,float)
ans = np.polyval(P,x)

print(ans)
