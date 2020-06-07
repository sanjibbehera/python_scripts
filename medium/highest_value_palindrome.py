###############################################################
#### Arguments to be passed to the program like below:-
#### python highest_order_palindrome.py
###############################################################

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    lo = 0
    hi = n-1
    diff = 0
    strgarr = []    
    mid = int(n/2)
    for idx in range(len(s)):
        strgarr.append(s[idx])
    
    x, y = 0, n-1
    while x<mid and y>=0:
        if (strgarr[x] != strgarr[y]):
            diff = diff + 1
        x += 1
        y -= 1    
    
    if (diff > k):
        return '-1'
    
    while(hi >= lo):
        if (k <= 0):
            break
        if (strgarr[lo] == strgarr[hi]):
            if (k > 1 and (k-2) >= diff and strgarr[lo] != '9'):
                strgarr[lo] = '9'
                strgarr[hi] = '9'
                k = k - 2
        else:
            if (k > 1 and (k-2) >= diff-1):
                if (strgarr[lo] != '9'):
                    strgarr[lo] = '9'
                    k = k - 1
                if (strgarr[hi] != '9'):
                    strgarr[hi] = '9'
                    k = k - 1
            else:
                if (strgarr[lo] > strgarr[hi]):
                    strgarr[hi] = strgarr[lo]
                else:
                    strgarr[lo] = strgarr[hi]
                k = k - 1
            diff = diff - 1
        if (lo == hi and k > 0):
            strgarr[lo] = '9'
            k = k - 1
        lo = lo + 1
        hi = hi - 1

    finalStr = ''.join(str(v) for v in strgarr)
    ans = isPalindrome(finalStr) 
  
    if ans: 
        return finalStr 
    else: 
        return '-1'

def isPalindrome(strg): 
    return strg == strg[::-1]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()
    result = highestValuePalindrome(s, n, k)
    print(result)

    #fptr.write(result + '\n')
    #fptr.close()