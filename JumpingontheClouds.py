#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c,n):
        c.append(2)
        jump = 0
        #dangerjump=c.count(1)
        i=0
        while n>=i+2 :
         if c[i] == 0 and c[i+1] ==0 and c[i+2] ==0: 
            i= i +2
            jump+=1
         elif c[i] == 0 and c[i+1] ==0: 
            i= i +1
            jump+=1
         elif c[i] == 0 and c[i+1] ==1:    
            i= i +2  
            jump+=1  
            
        return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    fptr.write(str(result) + '\n')

    fptr.close()
