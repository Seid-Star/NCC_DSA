a=int(input())
arr=list(map(int,input().split()))
brr=[]
crr=[]
drr=[]
for i in range(a):
    if arr[i]==1:
        brr.append(i+1)
    elif arr[i]==2:
        crr.append(i+1)
    else:
        drr.append(i+1)
b=min(len(brr),len(crr),len(drr))
print(b)
for x in range(b):
    print(brr[x],crr[x],drr[x
                            ])
