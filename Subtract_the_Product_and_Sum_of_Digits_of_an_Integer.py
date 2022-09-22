N=int(input())
p=1
s=0
while N>0:
    r=N%10
    p*=r
    s+=r
    e=p-s
    N=N//10
print(e)