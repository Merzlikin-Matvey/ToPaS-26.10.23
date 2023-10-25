from scipy.special import comb


def a(xi: int = 8):
    return comb(10, xi) * pow(0.04, 10 - xi) * pow(0.96, xi)


def b(n: int = 10, p: float = 0.8):
    success = p + (1 - p) * p
    return n * success


def c(n: int = 10, p: float = 0.8):
    return b(n, p) * (1 - (p + (1 - p) * p))


