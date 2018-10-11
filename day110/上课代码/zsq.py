def war(f):
    def inner(*args,**kwargs):
        a2 = args[0] * 2
        ret = f(a2)
        return ret
    return inner

@war # inner = war(f=func)
def func(a):
    print(a)
    return a


res = func(9) # inner(9)
print(res)


