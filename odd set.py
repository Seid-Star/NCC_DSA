a=int(input())
for x in range (a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=0
    d=0
    for i in arr:
        if i%2==0:
            c=c+1
        else:
            d=d+1
    if c==b and d==b:
        print("YES")
    else:
        print("NO")