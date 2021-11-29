a=int(input())
i=1
for i in range(1,a*2):
    if i<=a:
     print(i,end=" ")
    else:
        a=a-1
        print(a,end=" ")
    
