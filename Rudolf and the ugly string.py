a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    d=c.count("map")
    e=c.count("pie")
    f=c.count("mapie")
    g=d+e
    h=g-f
    print(h)
