a=int(input())
for x in range(a):
    b=int(input())
    c=str(b)
    i=1
    count=0
    while count<b:
        if i%3!=0 and (str(i)[-1])!='3':
            count+=1
            if count==b:
                print(i)
                break
        i+=1
