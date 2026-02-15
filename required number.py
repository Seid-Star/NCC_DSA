a=int(input())
for x in range(a):
    x,y,n=map(int,input().split())
    if n%x==y:
        print(n)
    else:
        c=n%x
        d=n-(c-y)
        if d>n:
            d=d-x
        print(d)
