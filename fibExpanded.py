zero = lambda f: lambda x: x
true = lambda x: lambda y: x
false = lambda x: lambda y: y
isZero = lambda n: n(lambda x: false)(true)
succ = lambda n: lambda f: lambda x: f((n)(f)(x))

def church2bool(b):
    return b(True)(False)
def church2int(c):
    return c(lambda x: x + 1)(0)
def int2church(i):
    if i == 0:
        return zero
    else:
        return succ(int2church(i - 1))
def PIR(f):
    def wrapperFunction(n):
        if church2bool(isZero(n)):
            return zero
        else:
            return f(n)
    return wrapperFunction

print(church2int((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: PIR(lambda n: (lambda m: lambda n: (lambda n: n(lambda x: (lambda x: lambda y: y))((lambda x: lambda y: x)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda x: x)))(m))(m)(n)))(n)((lambda f: lambda x: f(x)))(n)((lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x)))(f((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda x: x)))(m))(n)((lambda f: lambda x: f(x)))))(f((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda x: x)))(m))(n)((lambda f: lambda x: f(f(x)))))))))(int2church(10))))