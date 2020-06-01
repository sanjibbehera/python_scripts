###############################################################
#### Arguments to be passed to the program like below:-
#### python greedy_florist.py



#### For example, if there are k=3 friends that want to buy n=4 flowers that cost c=[1,2,3,4] each will buy one of the flowers priced [2,3,4] at the original price. 
#### Having each purchased x=1 flower, the first flower in the list, c[0], will now cost (current purchases + previous purchases) * c[0] = (1+1) * 1 = 2.
#### The total cost will be 2+3+4+2=11.
###############################################################

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, flowers):
    res = 0
    cnt = 0

    flowers = sorted(flowers, key=lambda x: -x)
    
    for el in flowers:
        res += el * (1 + cnt//k)
        cnt += 1
        
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
    #fptr.write(str(minimumCost) + '\n')
    #fptr.close()