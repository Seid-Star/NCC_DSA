a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=[0]*b
    count=0
    for i in arr:
        if i==-1:
            count=count+1
    if count==b:
        crr=[]
        for r in range(len(arr)-1):
            s=arr[r+1]-arr[r]
            crr.append(s)
            r=r+1
        print(abs(sum(crr)))
        print(*brr)
    elif arr[0]==-1 and arr[-1]==-1:
        arr[0]=0
        arr[-1]=0
        for z in range(len(arr)-1):
            if arr[z]==-1:
                arr[z]=0
        crr=[]
        for r in range(len(arr)-1):
            s=arr[r+1]-arr[r]
            crr.append(s)
            r=r+1
        print(abs(sum(crr)))
        print(*arr)
    elif arr[0]!=-1 and arr[-1]!=-1:
        for z in range(len(arr)-1):
            if arr[z]==-1:
                arr[z]=0
        crr=[]
        for r in range(len(arr)-1):
            s=arr[r+1]-arr[r]
            crr.append(s)
            r=r+1
        print(abs(sum(crr)))
        print(*arr)
    elif arr[0]!=-1 and arr[-1]==-1:
        for z in range(b):
            if arr[z]==-1:
                arr[z]=0
        brr=[]
        for y in range(b-1):
            h=arr[y+1]-arr[y]
            brr.append(h)
            y=y+1
        g=sum(brr)
        arr[-1]=abs(g)
        crr=[]
        for r in range(len(arr)-1):
            s=arr[r+1]-arr[r]
            crr.append(s)
            r=r+1
        print(abs(sum(crr)))
        print(*arr)
    elif arr[0]==-1 and arr[-1]!=-1:
        for z in range(b):
            if arr[z]==-1:
                arr[z]=0
        brr=[]
        for y in range(b-1):
            h=arr[y+1]-arr[y]
            brr.append(h)
            y=y+1
        g=sum(brr)
        arr[0]=abs(g)
        crr=[]
        for r in range(len(arr)-1):
            s=arr[r+1]-arr[r]
            crr.append(s)
            r=r+1
        print(abs(sum(crr)))
        print(*arr)
        
        
    
                
        
