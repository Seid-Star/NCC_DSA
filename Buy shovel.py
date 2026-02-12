a,b=map(int,input().split())
c=str(a)
if int(c[-1])==b or int(c[-1])==0:
    print(1)
else:
    d=2
    while True:
        e=a*d
        f=str(e)
        g=int(f[-1])
        if g==0 or g==b:
            print(d)
            break
        d=d+1
