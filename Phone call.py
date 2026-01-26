n=int(input())
arr=[]
for x in range(n):
   a=input().strip()
   arr.append(a)
b=arr[0]
for i in arr[1:]:
    while not i.startswith(b):
        b=b[:-1]
        if b== "":
            break
print(len(b))
