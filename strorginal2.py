def fun(s):
  dic={}
  for i in s:
    if i!=' ' and i not in dic:
      dic[i]=1
  
  return ''.join(list(dic.keys()))
s=input().lower()
res=fun(s)
print(res)
