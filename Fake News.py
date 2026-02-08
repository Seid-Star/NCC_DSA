a=input().strip()
b='heidi'
c=0
d=len(b)
e=''
for x in a:
    if c<d and b[c]==x:
        c+=1
        e+=x
if b==e:
    print("YES")
else:
    print("NO")
