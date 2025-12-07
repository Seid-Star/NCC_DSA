n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    dif=abs(a-b)
    print((dif+9)//10)