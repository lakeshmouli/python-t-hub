def fun(s):
  dic={}
  for i in s:
    if i!=' ':
      if i not in dic:
         dic[i]=1
      else:
        dic[i]+=1
  res=0
  for k,v in dic.items():
    if v==1:
      res+=1
  return res
s=input().lower()
res=fun(s)
print(res)
