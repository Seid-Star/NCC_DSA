a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    arr=[]
    for i in c:
        arr.append(i)
    brr=arr.copy()
    brr.reverse()
    i=0
    count=0
    while i<b//2:
        if arr[i]!=brr[i]:
            count+=2
            i+=1
        else:
            break
    print(b-count)
