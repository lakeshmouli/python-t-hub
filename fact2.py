def fun(n):
    if n<=0:
        print("*")
        return
    fun(n-1)
    fun(n-2)
fun(5)

