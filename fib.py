succ = lambda n: lambda f: lambda x: f((n)(f)(x))
pred = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda x: x)

add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
minus = lambda m: lambda n: n(pred)(m)

true = lambda x: lambda y: x
false = lambda x: lambda y: y

zero = lambda f: lambda x: x
one = succ(zero)
two = succ(one)

isZero = lambda n: n(lambda x: false)(true)
leq = lambda m: lambda n: is0(minus(m)(n))

Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

def church2int(c):
    return c(lambda x: x + 1)(0)

def int2church(i):
    if i == 0:
        return zero
    else:
        return succ(int2church(i - 1))

def church2bool(b):
    return b(True)(False)

def PIR(f):
    def wrapperFunction(n):
        if church2bool(isZero(n)):
            return zero
        else:
            return f(n)
    return wrapperFunction

fibonacci = Z(lambda f: PIR(lambda n: leq(n)(one)(n)(add(f(minus(n)(one)))(f(minus(n)(two))))))
print(church2int(fibonacci(int2church(10))))