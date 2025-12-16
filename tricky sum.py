a=int(input())
for x in range(a):
    b=int(input())
    T=b*(b+1)//2
    sump=0
    p=1
    while p<=b:
        sump=sump+p
        p=p*2
    print(T-2*sump)    