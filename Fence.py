a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=[]
for x in arr:
    if x>b:
        brr.append(2)
    else:
        brr.append(1)
print(sum(brr))

