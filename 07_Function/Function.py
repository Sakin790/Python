def fun1(msg):
    return(msg)

def fun2(func):
    return func

fun1("Hello World")
result=fun2(fun1)
print(result)