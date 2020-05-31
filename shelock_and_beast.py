##############################################################
#### Arguments to be passed to the program like below:-
#### python shelock_and_beast.py

#### A Decent Number has the following properties:

#### Its digits can only be 3's and/or 5's.
#### The number of 3's it contains is divisible by 5.
#### The number of 5's it contains is divisible by 3.
#### It is the largest such number for its length.
#### Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. 
#### Your task is to help Sherlock find the key before The Beast is destroyed!

#### For example, the numbers 55533333 and 555555 are both decent numbers because there are 3 5's and 5 3's in the first, and  6 5's in the second. 
#### They are the largest values for those length numbers that have proper divisibility of digit occurrences.
##############################################################

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(N):
    if (N < 3):
        return "-1"
    three_cnt = int(N/3)
    five_cnt = 0
    while three_cnt >=0:
        rem = N - three_cnt*3
        if int(rem % 5) == 0:
            five_cnt = int(rem/5)
            break
        three_cnt -= 1
    if three_cnt <= 0 and five_cnt == 0:
        return "-1"
    return "555"*three_cnt + "33333"*five_cnt

if __name__ == '__main__':
    t = int(input().strip())
    x = []

    for t_itr in range(t):
        n = int(input().strip())
        print(decentNumber(n))