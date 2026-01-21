a=int(input())
for x in range(a):
    b=input().strip()
    c=input().strip()
    d=0
    for i in range(1,len(c)):
        d=d+abs((b.index(c[i])-b.index(c[i-1])))
    print(d)
