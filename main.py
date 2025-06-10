def fun(x=0):
    return x**2

call = fun(6)
print(call)

y = lambda a : a * 5
print(y(5))

x = lambda a, b, c : a + b * (c + 5)
print(x(5, 5, 2))


def myfun(n):
    return lambda y=1 : y * n

mydoubler = myfun(2)
print(mydoubler)
print(mydoubler(5))
print(myfun(5)())
print(myfun(10)(2))