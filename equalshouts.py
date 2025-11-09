a,b=map(int,input().split())
c=0
d=0
for i in range(a):
    e,f=map(int,input().split())
    c=c+e*f
for i in range(b):
    g,h=map(int,input().split())
    d=d+g*h
if c==d:
    print("same")
else:
    print("different")