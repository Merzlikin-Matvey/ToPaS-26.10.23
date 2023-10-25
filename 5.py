from scipy.special import comb
import math

def a():
    ans = 0
    for i in range(100):
        ans += pow(0.9, 166) * pow(0.1, i) * comb(165 + i, i) * (166 + i)
    return ans


def b():
    return 2 * math.ceil(math.log(2 / 3, 0.9))


def c():
    E_a = pow(0.9, 4) + pow(0.9, 4) * 0.1 * comb(4, 1)
    return E_a - pow(E_a, 2)

print(c())

