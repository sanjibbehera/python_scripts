##############################################################
#### Arguments to be passed to the program like below:-
#### python beautiful-pairs.py

#### Function Description:-
#### Complete the beautifulPairs function in the editor below. 
#### It should return an integer that represents the maximum number of pairwise disjoint beautiful pairs that can be formed.

#### beautifulPairs has the following parameters:
#### A: an array of integers
#### B: an array of integers

#### Input Format:-
#### The first line contains a single integer n, the number of elements in A and B.
#### The second line contains n space-separated integers A[i].
#### The third line contains n space-separated integers B[i].
##############################################################

import math
import os
import random
import re
import sys
import collections

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    out_arr = []
    pairs = 0
    ac = collections.Counter(A)
    bc = collections.Counter(B)
    pairs = 0
    for val in ac:
        if val in bc:
            pairs += min(ac[val],bc[val])
    if pairs == len(A):
        pairs = pairs - 1
    else:
        pairs = pairs + 1
    return pairs


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    result = beautifulPairs(A, B)
    #fptr.write(str(result) + '\n')
    #fptr.close()