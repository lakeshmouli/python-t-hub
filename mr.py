n=int(input())
c=0
oc=0
ec=0
while n!=0:
    c+=1
    d=n%10
    n=n//10
    if d%2:
        oc+=1
    elif n%2==0:
        ec+=1
if ec==c:
    print("even")
elif oc==c:
    print("odd")
else:
    print("mixed")

    
