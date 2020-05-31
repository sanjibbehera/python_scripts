##############################################################
#### Arguments to be passed to the program like below:-
#### python staircase.py
#### Consider a staircase of size n=4.
#### Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. 
#### The last line is not preceded by any spaces.
#### Write a program that prints a staircase of size n.
##############################################################

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    ch_arr = []
    ch = ''
    for count in range(n):
        space_length = n - (count+1)
        ch += '#'
        string_length=len(ch)+space_length
        string_revised=ch.rjust(string_length)
        ch_arr.append(string_revised)
    return ch_arr

if __name__ == '__main__':
    n = int(input())
    output = staircase(n)
    for cnt in range(len(output)):
        print(output[cnt])