s=input()
d=list(s)
n=len(d)
i=1
d[0]=d[0].upper()
while i<n:
  if ord(d[i])>=65 and ord(d[i])<=90:
    d.insert(i,' ')
    i+=2
    n+=1
  else:
    i+=1
print(''.join(d))
