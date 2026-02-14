a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=[]
    count=0
    i=0
    while i<b:
        if arr[i]==0:
            count=count+1
        else:
            if count>0:
                brr.append(count)
            count=0
        if count>0:
            brr.append(count)
        i=i+1
    if len(brr)>0:
        print(max(brr))
    else:
        print(0)


    

    
