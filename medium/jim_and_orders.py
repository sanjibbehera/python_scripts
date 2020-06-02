###############################################################
#### Arguments to be passed to the program like below:-
#### python jim_and_orders.py

#### Function Description

#### Complete the jimOrders function in the editor below. It should return an array of integers that represent the order that customers' orders are delivered.

#### jimOrders has the following parameter(s):

#### orders: a 2D integer array where each orders[i] is in the form [order[i], prep[i]].
#### Input Format

#### The first line contains an integer n, the number of customers.
#### Each of the next n lines contains two space-separated integers, an order number and prep time for customer[i].

#### Constraints
#### 1 <= n <= 10^3
#### 1 <= i <= n
#### 1 <= oreder[i],prep[i] <= 10^6

#### Output Format

#### Print a single line of n space-separated customer numbers (recall that customers are numbered from 1 to n) that describes the sequence in which the 
#### customers receive their burgers. If two or more customers receive their burgers at the same time, print their numbers in ascending order.
###############################################################

import math
import os
import random
import re
import sys
from bisect import insort
from collections import defaultdict

# Complete the jimOrders function below.
def jimOrders(orders):
    sequence = []
    
    for idx, el in enumerate(orders, 1):
        tym = sum(el)
        insort(sequence, (tym, idx))
    
    return list(map(lambda x: x[1], sequence))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()