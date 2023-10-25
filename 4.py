from scipy.special import comb


def checker(ans: int, n: int = 200, p: float = 0.1):
    return round(sum([comb(ans, i) * pow(p, ans - i) * pow(1 - p, i) for i in range(n)]), 6) >= 0.99


n = 200
l = n
r = 2 * n

while r - l > 1:
    m = (r + l) // 2

    if checker(m):
        l = m
    else:
        r = m

print(l)
