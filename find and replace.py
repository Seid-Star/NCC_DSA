a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    e=set()
    o=set()
    G=True
    for i in range(len(c)):
        if i%2==0:
            if c[i] in o:
                G=False
                break
            e.add(c[i])
        else:
            if c[i] in e:
                G=False
                break
            o.add(c[i])
    if G:
        print("YES")
    else:
        print("NO")
            

