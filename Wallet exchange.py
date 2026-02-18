a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d=abs(b-c)
    if d%2==0:
        print("Bob")
    else:
        print("Alice")
