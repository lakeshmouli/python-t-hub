a,b=map(int,input().split())
res=0
while a:
    if a%2:
        res+=b
    a=a//2
    b=b*2
print(res)
