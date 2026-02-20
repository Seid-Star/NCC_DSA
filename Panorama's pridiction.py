a,b=map(int,input().split())
c=a+1
while True:
    d=True
    for i in range(2,c):
        if c%i==0:
            d=False
            break
    if d:
        break
    c+=1
if c==b:
    print("YES")
else:
    print("NO")



