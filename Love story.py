a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=[]
count=0
for i in arr:
    brr.append(i+b)
for x in brr:
    if x<=5:
        count+=1
print(count//3)



