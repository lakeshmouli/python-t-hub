def fun(S):
  res=''
  for i in s:
    if i!=' ' and i not in res:
      res+=i
    return res
s=input().lower()
res=fun(s)
print(res)
