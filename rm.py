n=int(input())
oc=0
ec=0
while n!=0:
         d=n%10
         n=n//10
         if d%2:
                 oc+=1
         else:
                 ec+=1
print(oc,ec)
