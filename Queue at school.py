a,b=map(int,input().split())
c=input().strip()
arr=[]
for i in c:
    arr.append(i)
while b>0:
    i=0
    while i<a-1:
        if arr[i]=='B' and arr[i+1]=='G':
            d=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=d
            i+=2
        else:
            i+=1
    b=b-1
print(''.join(arr))
