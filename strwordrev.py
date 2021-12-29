s=input()
d=s.split()
d[0]=d[0].upper()
d[::-1]
for i in range(len(d)):
  d[i]=d[i][::-1]
print(" ".join(d))
