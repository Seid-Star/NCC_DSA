a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    d=c.count('.')
    if "..." in c:
        print(2)
    else:
        print(d)

