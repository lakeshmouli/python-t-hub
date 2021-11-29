a,b=map(int,input().split())
res=0
while a:
    a=a//2
    b=b*2
    print(a,b)
    if a%2!=0:
        res+=b
    print(res)
