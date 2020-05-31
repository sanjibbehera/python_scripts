##############################################################
#### Arguments to be passed to the program like below:-
#### python plusMinus.py
#### It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.
#### If Input is:
#### 6
#### -4 3 -9 0 4 1
#### Output desired:-
#### positive: 3/6= 0.500000 , negative: 2/6= 0.333333, zeros: 1/6 = 0.166667
##############################################################

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    final_arr = []
    positive = 0
    negative = 0
    zeroes = 0
    length = len(arr)
    for count in range(length):
        if arr[count] > 0:
            positive+=1
        elif arr[count] < 0:
            negative+=1
        else:
            zeroes+=1
    finalPositive = "{:.6f}".format(positive/length)
    finalnegative = "{:.6f}".format(negative/length)
    finalzeroes   = "{:.6f}".format(zeroes/length)
    final_arr.append(finalPositive)
    final_arr.append(finalnegative)
    final_arr.append(finalzeroes)
    return final_arr

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    out_arr = plusMinus(arr)
    for cnt in range(len(out_arr)):
        print(out_arr[cnt])