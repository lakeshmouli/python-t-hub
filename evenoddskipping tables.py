num,r=map(int,input().split())
if num%2==0:
    s=1
else:
    s=2
for i in range(1,r+1,2):
    print(num,i,num*i)
