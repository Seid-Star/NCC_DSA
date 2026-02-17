a=int(input())
for x in range(a):
    b,c,d=map(int,input().split())
    e=(c*(c+1))//2
    g=(b*(b+1))//2
    f=g-(((b-c)*(b-c+1))//2)
    if e<=d<=f:
        print("YES")
    else:
        print("NO")
        

