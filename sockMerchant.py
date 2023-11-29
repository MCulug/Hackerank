#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar.sort()
    counter = 0
    #for _ in range (0,8):
    while len(ar) >1:
        if ar[0]==ar[1]:
         ar.pop(0)
         ar.pop(0)  
         counter+=1
        elif ar[0]!=ar[1]:
         ar.pop(0)
    print(counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
