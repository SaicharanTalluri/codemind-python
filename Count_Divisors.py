L,R,K=map(int,input().split())
c=0
for i in range(L,R+1):
    if i%K==0:
        c+=1
print(c)