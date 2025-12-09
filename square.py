a=int(input())
for x in range(a):
    c,d=map(int,input().split())
    e,f=map(int,input().split())
    g,h=map(int,input().split())
    i,j=map(int,input().split())
    if c!=e:
        dif=abs(c-e)
    elif c!=g:
        dif=abs(c-g)
    else:
        dif=abs(c-i)
    print(dif**2)		