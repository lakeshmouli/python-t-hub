s=input()
wc=0
for i in s:
  if ord(i)>=65 and ord(i)<=90:
    wc+=1
print(wc+1)
