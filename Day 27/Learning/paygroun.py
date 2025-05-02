def add(*args):
    print(type(args))
    print(args[3])
    num = 0
    for n in args:
        num +=n
    print(num)


##add(1,2,3,4,5,6)

def calculater(n, **kwargs):
    print(type(kwargs))
    print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key, value)
    n+=kwargs["add"]
    n*=kwargs["mul"]
    n-=kwargs["sub"]
    print(n)



calculater(2, add=3, mul=5, sub=2)