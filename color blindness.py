a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    d=input().strip()
    c=c.replace("G","B")
    d=d.replace("G","B")
    found=True
    for i in range(b):
        if c[i]!=d[i]:
            found=False
            break
    if found:
        print("YES")
    else:
        print("NO")
        
        
