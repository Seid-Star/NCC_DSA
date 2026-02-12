a=input().strip()
b=0
c=0
for x in range(len(a)):
    if a[x]==a[x].upper():
        b=b+1
    else:
        c=c+1
if b>c:
    print(a.upper())
else:
    print(a.lower())

