n=int(input())
for x in range(n):
    t=int(input())
    a,b,c=map(int,input().split())
    ok=False
    if t==1:
        if a==2 and b==3:
            ok=True
        elif a==3 and c==2:
            ok=True
    elif t==2:
        if a==3 and b==1:
            ok=True
        elif b==3 and c==1:
            ok=True
    elif t==3:
        if a==2 and c==1:
            ok=True
        elif b==1 and c==2:
            ok=True
    if ok:
        print("YES")
    else:
        print("NO")        
    
