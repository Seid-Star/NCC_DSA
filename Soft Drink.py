a,b,c,d,e,f,g,h=map(int,input().split())
A=((b*c)//g)//a
B=(d*e)//a
C=(f/h)//a
print(int(min(A,B,C)))

