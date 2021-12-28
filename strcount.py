s=input()
wc=0
for i in s:
  if ord(i)==32:
    wc+=1
print(wc+1)
