n,r=map(int,input().split())
if r%n==0:
    print(r//n)
else:
    L=r//n
    R=L+1
    if r-L*n==R*n:
        print(L,R)
    elif r-L*n>R*n-r:
        print(R)
    else:
        print(L)
