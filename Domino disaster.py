a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    c=c.replace('U','X')
    c=c.replace('D','U')
    c=c.replace('X','D')
    print(c)
