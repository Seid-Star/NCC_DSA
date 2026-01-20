a=int(input())
wor=[0,0,0]
arr=list(map(int,input().split()))
if len(arr)<=3:
    if max(arr)==arr[0]:
        print("chest")
    elif max(arr)==arr[1]:
        print("biceps")
    else:
        print("back")
else:
    for i in range(3):
        wor[i]=sum(arr[i::3])
    if max(wor)==wor[0]:
        print("chest")
    elif max(wor)==wor[1]:
        print("biceps")
    else:
        print("back")
