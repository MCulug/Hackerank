def myfunc(a):
   emptystr=''
   emptry=''
   array_length= len(a)
   for i in range(0,array_length,2):
    emptystr=emptystr+a[i]
   for i in range(1,array_length,2):
    emptry=emptry+a[i]
   print(emptystr+' '+emptry) 

if __name__ == '__main__':
    arr = []
    n = int(input().strip())
    for i in range (0,n):
     arr.append(list(map(str, input())))
     myfunc(arr[i])
