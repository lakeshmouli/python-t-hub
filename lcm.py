a,b=map(int,input().split())
t=2
Lcm=1
while True:
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        Lcm=Lcm*t
    else:
        t+=1
    if a<t or b<t:
        print(Lcm*a*b)
        break
