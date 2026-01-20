arr=list(map(int,input().split()))
arr.sort()
if arr[-1]>=(10+arr[0]):
    print("check again")
else:
    print("final",arr[1])
