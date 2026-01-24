a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    d=c.count('0')
    e=c.count('1')
    if b==1 or b==2 and c[0]!=c[1]:
        print("YES")
    else:
        print("NO")
