T=int(input())
for x in range(T):
    a,b,n=map(int,input().split())
    count=0
    while a<=n and b<=n:
        if a<b:
            a=a+b
        else:
            b=b+a
        count=count+1
    print(count)
