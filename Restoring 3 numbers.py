arr=list(map(int,input().split()))
brr=[]
e=max(arr)
for i in arr:
    if i!=e:
        brr.append(e-i)
print(*brr)

