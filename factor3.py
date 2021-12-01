from math import *

def fc(num,k):
    c=0
    for i in range(num,0,-1):
        if num%i==0:
            c+=1
        if k==c:
            return i
    return -1            
num,k=map(int,input().split())
print(fc(num,k))

   
