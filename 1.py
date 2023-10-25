from scipy.special import comb


def a(n: int = 5, k: int = 2, p: float = 0.24):
    ans = 0
    for k in range(k, n + 1):
        ans += comb(n, k) * pow(1 - p, n - k) * pow(p, k)

    return round(ans, 4)


def b(n: int = 16, p: float = 0.24):
    return round(n * p, 4)

