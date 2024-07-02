#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(a):
 new_array = []
 array_length= len(a)
 for i in range(array_length):
  new_array.append(int(a[(array_length-1)-i]))
 
 for i in range(array_length):
  print(new_array[i], end = " ")
 
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    reverse(arr)
