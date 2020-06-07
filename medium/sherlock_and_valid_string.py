###############################################################
#### Arguments to be passed to the program like below:-
#### python sherlock_and_valid_string.py
###############################################################

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    cnt = Counter(s)
    ret = 'NO'
    print(cnt)
    print("cnt = {} len = {}".format(cnt, len(set(cnt.values()))))

    if len(set(cnt.values())) == 1:
        ret = 'YES'
    elif len(set(cnt.values())) == 2:
        big_occur  = max(cnt.values())
        small_occur = min(cnt.values())
        print('big:',big_occur)
        print('small',small_occur)

        bigger_let = [let for let, c in cnt.items() if c == big_occur]
        smaller_let = [let for let, c in cnt.items() if c == small_occur]
        print(len(bigger_let))
        print(len(smaller_let))

        if len(smaller_let) == 1 and small_occur == 1:
            ret = 'YES'
        elif len(bigger_let) == 1 or len(smaller_let) == 1:
            if abs(big_occur-small_occur) == 1:
                ret = 'YES'
            else:
                ret = 'NO'
        else:
            ret = 'NO'
    else:
        ret = 'NO'

    return ret

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = isValid(s)
    print(result)
    #fptr.write(result + '\n')
    #fptr.close()