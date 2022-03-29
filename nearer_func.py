def fun(num,val):
  r1=val//num
  r2=r1+1
  if val-num*r1>num*r2-val:
    return r2
  return r1
num,val=map(int,input().split())
print(fun(num,val))
