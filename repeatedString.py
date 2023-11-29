#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(size, part):
    sizeofstr= len(part)
    print(sizeofstr)
    innercount=0
    lastinnercount=0
    fullcount = int(size/sizeofstr)
    for i in range (0,sizeofstr):
     if part[i]=="a":
       innercount+=1
    partcount = size%sizeofstr
    for i in range (0,partcount):
     if part[i]=="a":
        lastinnercount+=1
    
    subtotal=fullcount*innercount+lastinnercount
       
    print(subtotal)
    
    
if __name__ == '__main__':

    part = list(map(str, input().rstrip()))
    size = int(input())
    
    repeatedString(size, part)


