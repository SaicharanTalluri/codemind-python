A=int(input())
C=A*A
S=0
while C>0:
    R=C%10
    S+=R
    C=C//10
if S==A:
    print("Neon Number")
else:
    print("Not Neon Number")