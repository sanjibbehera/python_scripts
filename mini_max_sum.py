##############################################################
#### Arguments to be passed to the program like below:-
#### python mini_max_sum.py
#### Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
#### Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#### Our initial numbers are 1, 2, 3, 4 and 5. We can calculate the following sums using four of the five integers:

#### If we sum everything except 1, our sum is 2+3+4+5=14.
#### If we sum everything except 2, our sum is 1+3+4+5=13.
#### If we sum everything except 3, our sum is 1+2+4+5=12.
#### If we sum everything except 4, our sum is 1+2+3+5=11.
#### If we sum everything except 5, our sum is 1+2+3+4=10.

#### Hence Output will be 10 and 14
##############################################################

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    output_arr = []
    arr_len = len(arr)
    idx = 0

    while idx < arr_len:
        skip_sum = 0
        for count in range(len(arr)):
            if idx == count:
                continue
            else:
                skip_sum += arr[count]
        output_arr.append(skip_sum)
        idx = idx+1
    return output_arr

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    op_arr = miniMaxSum(arr)
    print(min(op_arr), max(op_arr))