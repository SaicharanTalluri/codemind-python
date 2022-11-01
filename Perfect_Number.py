A=int(input())
S=0
for i in range(1,A):
    if A%i==0:
        S+=i
if S==A:
    print("True")
else:
    print("False")