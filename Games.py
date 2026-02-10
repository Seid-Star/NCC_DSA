a=int(input())
arr=[]
brr=[]
for x in range(a):
    b,c=map(int,input().split())
    arr.append(b)
    brr.append(c)
count=0
for i in range(a):
    d=brr.count(arr[i])
    count+=d
print(count)


