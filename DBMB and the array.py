a=int(input())
for x in range(a):
    b,c,d=map(int,input().split())
    arr=list(map(int,input().split()))
    e=sum(arr)
    f=e-c
    if c==e:
        print("YES")
    elif c<e:
        print("NO")
    elif f%d==0:
        print("YES")
    else:
        print("NO")
    
