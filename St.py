a=int(input())
b=input().strip()
count=0
for i in range(a-1):
    if b[i]==b[i+1]:
        count=count+1
print(count)
