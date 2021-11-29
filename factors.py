import math
def factor_count(num):
    sq=int(math.sqrt(num))
    fc=2
    for i in range(2,sq+1):
        if num%i==0:
            fc+=1
            if i!=num//i:
                fc+=1
    return fc
num=int(input())
print(factor_count(num))
