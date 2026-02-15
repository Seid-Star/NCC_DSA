a=int(input())
for x in range(a):
    b=int(input())
    if b%3!=0:
        c=(b//3)+1
        d=b-((2*b//3))-1
    else:
        c=b//3
        d=b-(2*c)
    if c+(2*d)==b:
        print(c,d)
    else:
        print(d,c)
