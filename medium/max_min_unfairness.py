###############################################################
#### Arguments to be passed to the program like below:-
#### python max_min_unfairness.py

#### Function Description

#### Complete the maxMin function in the editor below. It must return an integer that denotes the minimum possible value of unfairness.

#### maxMin has the following parameter(s):
#### k: an integer, the number of elements in the array to create
#### arr: an array of integers .

#### Input Format
#### The first line contains an integer n, the number of elements in array arr.
#### The second line contains an integer k.
#### Each of the next n lines contains an integer arr[i] where 0<=i<n.
###############################################################

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    print(k)
    answer = 100000000000000000000
    
    for idx in range(len(arr)-k+1):
        diff = arr[idx+k-1] - arr[idx]
        if diff < answer:
            answer = diff
    return answer

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()