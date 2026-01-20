
n=int(input())
for x in range(n):
    a,b,c=list(map(int,input().split()))
    if a>b:
        print("First")
    elif a<b:
        print("Second")
    else:
        if c%2==1:
            print("First")
        else:
            print("Second")