from fractions import gcd

def rational(n, d):
    """
    returns a rational number x
    """
    g = gcd(n ,d)
    return [n // g, d // g]

def numer(x):
    """
    return the numerator of x
    """
    return x[0]

def denom(x):
    """
    return the denominator of x
    """
    return x[1]

def mul_rational(x, y):
    return rational(numer(x) * numer(y),
                    denom(x) * denom(y))

def add_rational(x ,y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def print_rational(x):
    print (numer(x), '/', denom(x))

def rational_is_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)