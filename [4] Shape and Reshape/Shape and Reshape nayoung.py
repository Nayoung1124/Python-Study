import numpy as np

a = list(map(int, input().strip().split(' ')))

my_array = np.array(a)

print(np.reshape(my_array,(3,3)))
