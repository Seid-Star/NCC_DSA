a=int(input())
arr=list(map(int,input().split()))
brr=[]
crr=[]
if 0 in arr:
    print(0)
elif a==1:
    if arr[0]>0:
        print(arr[0])
    else:
        print(0-arr[0])
        
else:
    for i in arr:
        if i>0:
            brr.append(i)
        else:
            crr.append(i)
    if len(brr)>0 and len(crr)>0:
        B=0-max(crr)            
        print(min(min(brr),B))
    elif len(brr)==0:
        print(0-max(crr))
    elif len(crr)==0:
        print(min(brr))
    
    

        
        
