a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    brr=[]
    crr=[]
    if len(set(arr))==1:
        print(-1)
    else:
        c=arr[0]
        for i in arr:
            if c==i:
                brr.append(c)
            else:
                crr.append(i)
        print(len(brr),len(crr))
        print(*brr)
        print(*crr)
