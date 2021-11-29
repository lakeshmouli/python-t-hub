n,r=map(int,input().split())#3 4
while True:
     if n==1:
        break
     if n%2:
        n=n*3+1
     elif n%2==0:
        n=n//2
     if n==r:
        print(True)
        break
     else:
        print(False)
        break
