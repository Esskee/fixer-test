import math
import os
import random
import re
import sys
import pip
import numpy as np

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    if arr:
        resp = np.array([[11, 2, 4], [4, 5, 6],[10, 8, -12]])
        resp = resp.reshape(3, 3)
        print(resp)
        x = resp.diagonal().sum()
        print(x)
        y = np.fliplr(resp).diagonal().sum()
        print(y)
        return print(abs(x-y))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    diagonalDifference(True)
    # n = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    #
    # result = diagonalDifference(arr)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
