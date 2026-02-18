a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=[]
    crr=[]
    found=True
    for i in arr:
        if i>c:
            found=False
    if found:
        print("YES")
    else:
        for i in arr:
            if i<c:
                brr.append(i)
            else:
                crr.append(i)
        brr.sort()
        if len(brr)>=2:
            if brr[0]+brr[1]<=c:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
        
    
