a=int(input())
arr=list(map(int,input().split()))
brr=[]
crr=[]
while a>0:
    if arr[0]>=arr[-1]:
        b=arr[0]
        arr.pop(0)
    else:
        b=arr[-1]
        arr.pop()
    brr.append(b)
    a=a-1
    if a==0:
        break
    if arr[0]>=arr[-1]:
        c=arr[0]
        arr.pop(0)
    else:
        c=arr[-1]
        arr.pop()
    crr.append(c)
    a=a-1
print(sum(brr),sum(crr))



