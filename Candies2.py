a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=min(arr)
    d=0
    for i in arr:
        d=d+(i-c)
    print(d)
