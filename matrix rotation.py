n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    ok=False
    for i in range(4):
        if a<b and a<c and c<d and b<d:
            ok=True
            break
        a,b,d,c=c,a,b,d
    if ok:
        print("YES")
    else:
        print("NO")    