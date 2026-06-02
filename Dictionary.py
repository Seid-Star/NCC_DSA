a=int(input())
for x in range(a):
    b=input()
    if b[1]>b[0]:
        print(((ord(b[1])-97))+(ord(b[0])-97)*25)
    else:
        c=((ord(b[1])-97))+(ord(b[0])-97)*25+1
        print(c)
