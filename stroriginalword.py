def fun(s):
  dic={}
  for i in s:
    if i!=' ' and i not in dic:
      dic[i]=1
  res=''
  for k in dic.keys():
    res+=k
  return res
s=input().lower()
res=fun(s)
print(res)
