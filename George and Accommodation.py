a=int(input())
count=0
for x in range(a):
    b,c=map(int,input().split())
    if (c-b)>=2:
        count+=1
print(count)
