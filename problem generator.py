a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d=input().strip()
    e=0
    for i in "ABCDEFG":
        f=d.count(i)
        if f<c:
            e=e+(c-f)
    print(e)