a,b=map(int,input().split())
if a>b:
    a,b=b,a
while a:
    b=b%a
    a,b=b,a
print(b)
