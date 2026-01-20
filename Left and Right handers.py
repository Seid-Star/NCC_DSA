l,r,a=map(int,input().split())
if l==0 and a==0 or r==0 and a==0:
    print(0)
else:
    if l==r:
        print((l+r)+(a//2)*2)
    else:
        if l>r:
            if (l-r)>a:
                print((r+a)*2)
            else:
                print((2*l)+(((a-(l-r))//2)*2))
        else:
            if (r-l)>=a:
                print((l+a)*2)
            else:
                print(((((2*r)))+(((a-(r-l))//2)*2)))
                


