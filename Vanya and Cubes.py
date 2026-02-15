a=int(input())
arr=[1]
b=sum(arr)
c=1
while b<a:
    c+=1
    arr.append(arr[-1]+c)
    b=sum(arr)
if b>a:
    arr.pop()
print(len(arr))
