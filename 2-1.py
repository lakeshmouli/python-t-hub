n=int(input())
c=0
while n!=0:
    d=n%10
    n=n//10
    if n%2:
        c+=1
    else:
