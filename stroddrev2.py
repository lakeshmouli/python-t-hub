s=input()
d=s.split()
wc=0
for i in range(len(d)):
  if len(d[i])%2==0:
    d[i]=d[i][::-1]
  
print(" ".join(d))
    
