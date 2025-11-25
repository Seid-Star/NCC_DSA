a=input()
b=0
c=0
for i in a:
    if i.isupper():
        b=b+1
    elif i.islower():
        c=c+1
if b>c:
    print(a.upper())
else:
    print(a.lower())