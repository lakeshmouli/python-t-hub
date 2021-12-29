s=input()
d=s.split()
v="aeiouAEIOU"
j=0
for i in d:
  if i[0] in v:
    d[j]=i[::-1]
  j+=1
print(" ".join(d))
