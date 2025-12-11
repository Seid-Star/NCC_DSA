a=0
b=0
c=0
for x in range(3):
    s=input()
    if s[1]==">":
        if s[0]=="A":
            a=a+1
        if s[0]=="B":
            b=b+1
        if s[0]=="C":
            c=c+1
    else:
        if s[2]=="A":
            a=a+1
        if s[2]=="B":
            b=b+1
        if s[2]=="C":
            c=c+1    
if a==b or a==c or b==c:
    print("Impossible")
else:
    if a==0:print("A",end="")  
    if b==0:print("B",end="")
    if c==0:print("C",end="")
    if a==1:print("A",end="")
    if b==1:print("B",end="")
    if c==1:print("C",end="")
    if a==2:print("A",end="")
    if b==2:print("B",end="")
    if c==2:print("C",end="")