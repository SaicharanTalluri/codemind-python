A=int(input())
B=int(input())
s=0
c=0
for i in range(1,A):
    if A%i==0:
        s+=i
for i in range(1,B):
    if B%i==0:
        c+=i
if s==B:
    print("Amicable")
elif c==A:
    print("Amicable")
else:
    print("Not Amicable")