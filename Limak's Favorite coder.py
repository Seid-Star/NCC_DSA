a=int(input())
arr=list(map(int,input().split()))
if a==1:
    print(0)
elif a==2:
    if arr[0]!=arr[1]:
        print(1)
    else:
        print(0)
else:
    Min=min(arr[0],arr[1])
    Max=max(arr[0],arr[1])
    b=2
    if Max==Min:
        count=0
    else:
        count=1
    for i in range(a-2):
        if arr[b]>Max:
            Max=arr[b]
            count+=1
        if arr[b]<Min:
            Min=arr[b]
            count+=1
        b+=1
    print(count)
    

