n=int(input())
next_prime=n
while True:
    fc=0
    for i in range(1,next_prime+1):
        if next_prime%i==0:
            fc+=1
    if fc==2:
        break
    next_prime+=1
previous_prime=n
while True:
    fc=0
    for i in range(1,previous_prime+1):
        if previous_prime%i==0:
            fc+=1
    if fc==2:
        break
    previous_prime-=1
if n-previous_prime<=next_prime-n:
    print(n-previous_prime)
else:
    print(next_prime-n)