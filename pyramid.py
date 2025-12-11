a=int(input())
p=1
count=0
while a>=p*(p+1)//2:
    a=a-p*(p+1)//2
    p=p+1
    count=count+1
print(count)    