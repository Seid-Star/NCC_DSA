a=int(input())
arr=[]
for x in range(a):
    b=int(input())
    arr.append(b)
count=1
for i in range(a-1):
    if arr[i]!=arr[i+1]:
        count=count+1
print(count)
