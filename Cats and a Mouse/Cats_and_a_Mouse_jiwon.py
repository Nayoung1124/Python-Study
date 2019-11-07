#!/bin/python3

import os

# x:Cat A  y:Cat B  z:Mouse C
def catAndMouse(x, y, z):
    x_z_distance = abs(x-z)
    y_z_distance = abs(y-z)
    
    if x_z_distance < y_z_distance:
        return 'Cat A'
    elif x_z_distance > y_z_distance:
        return 'Cat B'
    else:
        return 'Mouse C'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')
    fptr.close()
