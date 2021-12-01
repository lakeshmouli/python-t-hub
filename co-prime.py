def gcd(a,b):
    while True:
        if a>b:
            a,b=b,a
        b=b%a
        if b==0:
            return a

a,b=map(int,input().split())
if (a%2 or b%2) and gcd(a,b)==1:
    print("co-Primes")
else:
    print("Not  co-Prime")
