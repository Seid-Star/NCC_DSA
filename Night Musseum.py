A=input().strip()
B='a'
count=0
if B=='a':
    C=1
if B=='b':
    C=2
if B=='c':
    C=3
if B=='d':
    C=4
if B=='e':
    C=5
if B=='f':
    C=6
if B=='g':
    C=7
if B=='h':
    C=8
if B=='i':
    C=9
if B=='j':
    C=10
if B=='k':
    C=11
if B=='l':
    C=12
if B=='m':
    C=13
if B=='n':    
    C=14
if B=='o':
    C=15
if B=='p':
    C=16
if B=='q':
    C=17
if B=='r':
    C=18
if B=='s':
    C=19
if B=='t':
    C=20
if B=='u':
    C=21
if B=='v':
    C=22
if B=='w':
    C=23
if B=='x':
    C=24
if B=='y':
    C=25
if B=='z':
    C=26
for X in A:
    if X=='a':
        D=1
    if X=='b':
        D=2
    if X=='c':
        D=3
    if X=='d':
        D=4
    if X=='e':
        D=5
    if X=='f':
        D=6
    if X=='g':
        D=7
    if X=='h':
        D=8
    if X=='i':
        D=9
    if X=='j':
        D=10
    if X=='k':
        D=11
    if X=='l':
        D=12
    if X=='m':
        D=13
    if X=='n':
        D=14
    if X=='o':
        D=15
    if X=='p':
        D=16
    if X=='q':
        D=17
    if X=='r':
        D=18
    if X=='s':
        D=19
    if X=='t':
        D=20
    if X=='u':
        D=21
    if X=='v':
        D=22
    if X=='w':
        D=23
    if X=='x':
        D=24
    if X=='y':
        D=25
    if X=='z':
        D=26       
    E=abs(C-D)
    F=26-E
    G=min(abs(E),abs(F))
    count=count+G
    C=D
print(count)

