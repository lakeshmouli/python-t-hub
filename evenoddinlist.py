n=int(input())
data=list(map(int,input().split()))
os=0
es=0
for i in data:
    if i%2:
        os+=i
    else:
        es+=i
print(es,os)
