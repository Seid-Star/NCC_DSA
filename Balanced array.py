a=int(input())
for x in range(a):
    b=int(input())
    c=b//2
    arr=[]
    brr=[]
    crr=[]
    if c%2!=0:
        print("NO")
    else:
        for i in range(1,c+1):
            arr.append(2*i)
        for i in range(1,c):
            brr.append(2*i-1)
        d=sum(arr)
        e=sum(brr)
        f=d-e
        for i in arr:
            crr.append(i)
        for i in brr:
            crr.append(i)
        crr.append(f)
        print("YES")
        print(*crr)
        
        



