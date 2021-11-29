from math import*
def fc(num):
    c=0
    sq=int(sqrt(num))
    for i in range(1,sq+1):
        if num%i==0:
            print(i,num//i)
            c+=2
    if num==sq*sq:
        c-=1
    return c
num=int(input())
print(fc(num))
