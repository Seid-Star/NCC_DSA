a=input().strip()
b=input().strip()
count=0
c=len(b)
for x in range(c):
    if b[x]==a[count]:
        count=count+1
print(count+1)

