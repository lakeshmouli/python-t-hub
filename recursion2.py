def fun(n):
    if n<=0:
        return 1
    return fun(n-1)+(n-2)
print(fun(5))
