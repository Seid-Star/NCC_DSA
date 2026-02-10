a=input().strip('{}')
if a=="":
    print(0)
else:
    b=a.split(',')
    b=[x.strip() for x in b]
    print(len(set(b)))
    


