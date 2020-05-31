##############################################################
#### Arguments to be passed to the program like below:-
#### python diagonal_diff_square_matrix.py
#### Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.
#### If Input is:
#### 1 2 3
#### 4 5 6
#### 9 8 9
#### Output desired:-
#### The left-to-right diagonal 1+5+9= 15. The right to left diagonal 3+5+9= 17. Their absolute difference is |15 - 17| = 2.
##############################################################

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    rhs_sum = 0
    lhs_sum = 0
    length = len(arr[0])
    for count in range(length):
        rhs_sum += arr[count][count]
        lhs_sum += arr[count][(length-count-1)]
    return abs(rhs_sum-lhs_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
