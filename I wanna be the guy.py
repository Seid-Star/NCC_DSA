a=int(input())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
crr=arr[1:]+brr[1:]
b=len(set(crr))
if b==a:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
