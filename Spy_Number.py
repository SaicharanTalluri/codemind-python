N=int(input())
s=0
p=1
while N>0:
    r=N%10
    s+=r
    p*=r
    N=N//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")