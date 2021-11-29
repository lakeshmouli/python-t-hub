
n,r=map(int,input().split())
c=0
while True:
    c+=1
    if n==1:
        break
    if n%2:
        n=3*n+1
    else:
        n=n//2
print(c)
    
