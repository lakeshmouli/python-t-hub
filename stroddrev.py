s=input()
d=s.split()
c=0
for i in range(len(d)):
  if i%2==0:
    d[i]=d[i][::-1]
print(" ".join(d))
