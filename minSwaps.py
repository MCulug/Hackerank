#!/bin/python3

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    laststate = list(range(1,(len(arr)+1)))
    swaps= int()
    if arr == laststate:
        print('0') 
    else:
     while arr != laststate:
       for i in range (len(arr)-1):
         if arr[i]!=laststate[i]:
          sw=arr.index(i+1)
          arr[i],arr[sw]=arr[sw],arr[i]
          swaps+=1
       print(swaps) 

    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
