a=input().strip()
b=input().strip()
c=a.replace('0','')
d=b.replace('0','')
e=int(a)+int(b)
g=int(str(e).replace('0',''))
f=int(c)+int(d)
if g==f:
    print("YES")
else:
    print("NO")
