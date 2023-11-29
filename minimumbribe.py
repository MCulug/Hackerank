def minimumBribes(q):
    # Write your code here
    size=len(q)
    order=1
    flag=0
    for i in range (0,size):
        if q[i] != order:
         bribecount= q[i]-order
         if bribecount > 2:
            flag=1
            print("Too chaotic")
         order+=1
        else:
         order+=1 
    if flag==0:
            print("Not Too chaotic")
