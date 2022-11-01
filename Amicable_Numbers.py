A=int(input())
B=int(input())
S=0
D=0
for i in range(1,A):
    if A%i==0:
        S+=i
for j in range(1,B):
    if B%j==0:
        D+=j
if A==D and B==S:
    print("Amicable")
else:
    print("Not Amicable")
        