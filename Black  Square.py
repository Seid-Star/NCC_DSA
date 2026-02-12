arr=list(map(int,input().split()))
brr=[]
b=input().strip()
for x in b:
    brr.append(arr[int(x)-1])
print(sum(brr))
