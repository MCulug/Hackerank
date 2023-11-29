#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#



def myfunc(a, b, int_k):
   answer=0
   array_length= len(a)
   for i in range(array_length):
    array_a=a[i]
    array_b=b[array_length-1-i]
    presum=str(array_a)+str(array_b)
    final = int(presum)
    if k>final :
     answer+=1  
   print(answer)
      
    
if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    k = int(input())
    myfunc(a,b,k)


