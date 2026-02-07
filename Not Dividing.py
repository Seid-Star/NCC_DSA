a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    if b==1:
        print(*arr)
        continue
    for y in range(b):
        if arr[y]==1:
            arr[y]=2
    for i in range(b-1):
        if arr[i+1]%arr[i]==0:
             arr[i+1]=arr[i+1]+1
    print(*arr)
