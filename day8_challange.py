n = int(input().strip())
arr=[]
marr=[]
karr=[]
for i in range (0,n):
 arr.append(input().split())
 marr.append(arr[i][0])
 karr.append(arr[i][1])

while True:
 try:
  name = input().strip()
  if name in marr:
    print(name, "=", karr[marr.index(name)], sep="") 
  else: 
    print("Not found") 
 except EOFError:
  break;
