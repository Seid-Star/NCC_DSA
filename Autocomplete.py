a=input().strip()
b=int(input())
d=[]
for x in range(b):
    c=input().strip()
    if c.startswith(a):
        d.append(c)
if len(d)>0:
    print(min(d))
else:
    print(a)
