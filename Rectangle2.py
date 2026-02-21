a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d=max(2*c,b)
    e=max(c,2*b)
    f=min(d,e)
    print(f**2)
