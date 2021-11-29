n,m=map(int,input().split())
for i in range(1,m):
    if n*i<m:
      print(n,"X",i,"=",n*i)
    else:
        break
    
