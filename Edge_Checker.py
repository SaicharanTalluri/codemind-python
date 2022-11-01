A,B=map(int,input().split())
if A-B==1 or B-A==1:
    print("Yes")
elif A-B==9 or B-A==9:
    print("Yes")
else:
    print("No")