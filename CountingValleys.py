#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    # Write your code here
        level = 0
        levelprevious = 0
        valey = 0
        for i in range (0,(steps)):
         if path[i] == "U":
            levelprevious = level
            level +=1
         if path[i] == "D":
            levelprevious = level
            level = level - 1
         if levelprevious < 0 and level >= 0:
            valey +=1 
        return valey


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = list(map(str, input().rstrip()))

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
