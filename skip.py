n,n2=map(int,input().split())
for i in range(1,n2+1):
    if i%n==0:
        continue
    print(n,"X",i,"=",n*i)
